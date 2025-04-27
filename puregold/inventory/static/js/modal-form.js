var modal = document.getElementById("openAddBtn");

var btn = document.getElementById("addbtn");

var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "flex";
//   modal.style.height = "100%";
}

span.onclick = function() {
    modal.style.display = "none";
    // modal.style.height = "0";
}

window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container'); 

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none"; 
        }
    });
};



