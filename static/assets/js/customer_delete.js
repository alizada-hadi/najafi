const customerbtns = [...document.getElementsByClassName("delete-btns")]
const customermodalHeader = document.getElementById("modal-header")
const customermodalBody = document.getElementById("modal-body")
const customerdelInput = document.getElementById("customer_id")


customerbtns.forEach(btn => btn.addEventListener("click", () => {
    const pk = btn.getAttribute("data-id")
    const first = btn.getAttribute("data-name")
    const last = btn.getAttribute("data-last")

    customerdelInput.value = pk
    customermodalHeader.innerHTML = `
        <h3>Delete ${first} ${last} ?</h3>
    `
    
}))