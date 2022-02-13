const farmerbtns = [...document.getElementsByClassName("delete-btns")]
const farmermodalHeader = document.getElementById("modal-header")
const farmermodalBody = document.getElementById("modal-body")
const farmerdelInput = document.getElementById("farmer_id")


farmerbtns.forEach(btn => btn.addEventListener("click", () => {
    const pk = btn.getAttribute("data-id")
    const first = btn.getAttribute("data-name")
    const last = btn.getAttribute("data-last")

    farmerdelInput.value = pk
    farmermodalHeader.innerHTML = `
        <h3>Delete ${first} ${last} ?</h3>
    `
    
}))