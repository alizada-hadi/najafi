const buybtns = [...document.getElementsByClassName("delete-btns")]
const buymodalHeader = document.getElementById("modal-header")
const buymodalBody = document.getElementById("modal-body")
const buydelInput = document.getElementById( "buy_id")

 buybtns.forEach(btn => btn.addEventListener("click", () => {
    const pk = btn.getAttribute("data-id")
    const first = btn.getAttribute("data-name")
    const last = btn.getAttribute("data-last")

 buydelInput.value = pk
 buymodalHeader.innerHTML = `
        <h3>Delete ${first} ${last} ?</h3>
    `
    
}))