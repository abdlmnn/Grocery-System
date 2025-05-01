

// Category EDIT MODAL
const openEditModalCategory = async (id) => {
    const editModal = document.getElementById('openEditModalCategory');
    const editForm = document.getElementById('editForm');
    const nameEdit = document.getElementById('nameEdit');
    try {
        const res = await fetch(`/inventory/viewcategory/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data)

            if (data.status === 'success') {
                editModal.style.display = 'flex';
                nameEdit.value = data.name;
            } else {
                console.log('Error: ', data.message);
            }

            editForm.action = `/inventory/editcategory/${id}/`;

            editForm.onsubmit = async (e) => {
                e.preventDefault();

                const formData = new FormData(editForm);

                try {
                    const res = await fetch(editForm.action, {
                        method: 'POST',
                        body: formData,
                    });

                    if (res.ok) {
                        const data = await res.json();

                        console.log(data)

                        if (data.status === 'success') {
                            console.log('Message: ', data.message);
                            window.location.reload();
                        } else {
                            console.log('Message: ', data.message);
                        }
                    } else {
                        console.log('Something went wrong.');
                    }
                } catch (error) {
                    console.log('Error: ', error);
                }
            };
            

        } else {
            console.log('Something went wrong.');
        }
    } catch (error) {   
        console.log('Error: ', error);
    }

};
// Category EDIT MODAL


// Category VIEW MODAL
const openViewModalCategory = async (id) => {
    const viewModal = document.getElementById('openViewModalCategory');
    const nameView = document.getElementById('nameView');
    try {
        const res = await fetch(`/inventory/viewcategory/${id}/`);

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
    document.getElementById('openEditModalCategory').style.display = 'none';
}


window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container');

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};