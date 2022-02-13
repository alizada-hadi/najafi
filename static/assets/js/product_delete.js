const prodcutbtns = [...document.getElementsByClassName("delete-btns")]
const prodcutmodalHeader = document.getElementById("modal-header")
const prodcutmodalBody = document.getElementById("modal-body")
const prodcutdelInput = document.getElementById("prodcut_id")


prodcutbtns.forEach(btn => btn.addEventListener("click", () => {
    const pk = btn.getAttribute("data-id")
    const first = btn.getAttribute("data-name")
    const last = btn.getAttribute("data-last")

    prodcutdelInput.value = pk
    prodcutmodalHeader.innerHTML = `
        <h3>Delete ${first} ${last} ?</h3>
    `
    
}))