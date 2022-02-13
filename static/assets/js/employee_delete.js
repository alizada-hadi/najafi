const btns = [...document.getElementsByClassName("delete-btns")]
const modalHeader = document.getElementById("modal-header")
const modalBody = document.getElementById("modal-body")
const delInput = document.getElementById("employee-id")


btns.forEach(btn => btn.addEventListener("click", () => {
    const pk = btn.getAttribute("data-id")
    const first = btn.getAttribute("data-name")
    const last = btn.getAttribute("data-last")

    delInput.value = pk

    modalHeader.innerHTML = `
        <h3>Delete ${first} ${last} ?</h3>
    `
    
}))
