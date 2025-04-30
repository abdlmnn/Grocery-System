

// Category VIEW MODAL
const openViewModalCategory = async (id) => {
    const viewModal = document.getElementById('openViewModalCategory');
    const nameView = document.getElementById('nameView');
    try {
        const res = await fetch(`/inventory/viewcategory/${id}`);

        if (res.ok) {
            const data = await res.json();

            console.log(data); 

            if (data.status === 'success') {
                viewModal.style.display = 'flex';
                nameView.value = data.name;
            } else {
                console.log('Error: ', data.message);
            }
        } else {
            console.log('Something went wrong.');
        }
    } catch (error) {
        console.log('Error: ', error);
    }
};
// Category VIEW MODAL


function closeModal() {
    document.getElementById('openViewModalCategory').style.display = 'none';
}


window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container');

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};