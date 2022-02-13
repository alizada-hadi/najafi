const salebtns = [...document.getElementsByClassName("delete-btns")]
const salemodalHeader = document.getElementById("modal-header")
const salemodalBody = document.getElementById("modal-body")
const saledelInput = document.getElementById("sale_id")


salebtns.forEach(btn => btn.addEventListener("click", () => {
    const pk = btn.getAttribute("data-id")
    const first = btn.getAttribute("data-name")
    const last = btn.getAttribute("data-last")

    saledelInput.value = pk
    salemodalHeader.innerHTML = `
        <h3>Delete ${first} ${last} ?</h3>
    `
    
}))