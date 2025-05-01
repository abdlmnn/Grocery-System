

// Unit EDIT MODAL
const openEditModalUnit = async (id) => {
    const editModal = document.getElementById('openEditModalUnit');
    const editForm = document.getElementById('editForm');
    const nameEdit = document.getElementById('nameEdit');
    const abbreviationEdit = document.getElementById('abbreviationEdit');
    const descriptionEdit = document.getElementById('descriptionEdit');
    try {
        const res = await fetch(`/inventory/viewunit/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data)

            if (data.status === 'success') {
                editModal.style.display = 'flex';
                nameEdit.value = data.name;
                abbreviationEdit.value = data.abbreviation;
                descriptionEdit.value = data.description;
            } else {
                console.log('Error: ', data.message);
            }

            editForm.action = `/inventory/editunit/${id}/`;

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
// Unit EDIT MODAL


// Unit VIEW MODAL
const openViewModalUnit = async (id) => {
    const viewModal = document.getElementById('openViewModalUnit');
    const nameView = document.getElementById('nameView');
    const abbreviationView = document.getElementById('abbreviationView');
    const descriptionView = document.getElementById('descriptionView');
    try {
        const res = await fetch(`/inventory/viewunit/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data); 

            if (data.status === 'success') {
                viewModal.style.display = 'flex';
                nameView.value = data.name;
                abbreviationView.value = data.abbreviation;
                descriptionView.value = data.description;
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
// Unit VIEW MODAL


function closeModal() {
    document.getElementById('openViewModalUnit').style.display = 'none';
    document.getElementById('openEditModalUnit').style.display = 'none';
}


window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container');

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};