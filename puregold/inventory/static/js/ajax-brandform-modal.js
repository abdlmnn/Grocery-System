

// Brand EDIT MODAL
const openEditModalBrand = async (id) => {
    const editModal = document.getElementById('openEditModalBrand');
    const editForm = document.getElementById('editForm');
    const nameEdit = document.getElementById('nameEdit');
    try {
        const res = await fetch(`/inventory/viewbrand/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data)

            if (data.status === 'success') {
                editModal.style.display = 'flex';
                nameEdit.value = data.name;
            } else {
                console.log('Error: ', data.message);
            }

            editForm.action = `/inventory/editbrand/${id}/`;

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
// Brand EDIT MODAL


// Brand VIEW MODAL
const openViewModalBrand = async (id) => {
    const viewModal = document.getElementById('openViewModalBrand');
    const nameView = document.getElementById('nameView');
    try {
        const res = await fetch(`/inventory/viewbrand/${id}/`);

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
// Brand VIEW MODAL


function closeModal() {
    document.getElementById('openViewModalBrand').style.display = 'none';
    document.getElementById('openEditModalBrand').style.display = 'none';
}


window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container');

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};