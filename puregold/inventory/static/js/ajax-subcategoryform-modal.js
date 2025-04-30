

// Subcategory EDIT MODAL
const openEditModalSub = async (id) => {
    const editModal = document.getElementById('openEditModalSub');
    const editForm = document.getElementById('editForm');
    const categoryEdit = document.getElementById('categoryEdit');
    const nameEdit = document.getElementById('nameEdit');
    try {
        const res = await fetch(`/inventory/viewsubcategory/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data)

            if (data.status === 'success') {
                editModal.style.display = 'flex';
                categoryEdit.value = data.category;
                nameEdit.value = data.name;

                for (let option of categoryEdit.options) {
                    if (option.text === data.category) {
                        option.selected = true; 
                        break;
                    }
                }

                editForm.action = `/inventory/editsubcategory/${id}/`;

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
                console.log('Error: ', data.message);
            }

        } else {
            console.log('Something went wrong.');
        }
    } catch (error) {   
        console.log('Error: ', error);
    }

};
// Subcategory EDIT MODAL


// Subcategory VIEW MODAL
const openViewModalSub = async (id) => {
    const viewModal = document.getElementById('openViewModalSub');
    const categoryView = document.getElementById('categoryView');
    const nameView = document.getElementById('nameView');
    try {
        const res = await fetch(`/inventory/viewsubcategory/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data); 

            if (data.status === 'success') {
                viewModal.style.display = 'flex';
                categoryView.value = data.category;
                nameView.value = data.name;
                console.log('Message: ', data.message);
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
// Subcategory VIEW MODAL


function closeModal() {
    document.getElementById('openViewModalSub').style.display = 'none';
    document.getElementById('openEditModalSub').style.display = 'none';
}


window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container');

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};