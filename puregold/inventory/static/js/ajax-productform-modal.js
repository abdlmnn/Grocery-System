
// Product VIEW MODAL
const openViewModalProduct = async (id) => {
    const viewModal = document.getElementById('viewModal');
    const subcategory = document.getElementById('subcategory2'); 
    const brand = document.getElementById('brand2');
    const name = document.getElementById('name');
    const description = document.getElementById('description');
    const preview = document.getElementById('previewImage');
    try {
        const res = await fetch(`/inventory/viewproduct/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data); 

            if (data.status === 'success') {
                viewModal.style.display = "flex";

                subcategory.innerText = data.subcategory;
                brand.innerText = data.brand;
                
                name.value = data.name; 
                
                description.value = data.description;
                
                if (data.image) {
                    preview.src = data.image; 
                } else {
                    console.log('No image found.');
                }
            } else {
                console.log('Message', data.message);
            }
        } else {
            console.error('Something went wrong.');
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

function closeViewModal() {
    document.getElementById('viewModal').style.display = 'none';
}
// Product VIEW MODAL






// Product EDIT MODAL
const openEditModalProduct = async (id) => {
    const editModal = document.getElementById('editModal');
    const subcategory = document.getElementById('subcategory1'); 
    const brand = document.getElementById('brand1');
    const name = document.getElementById('productName1');
    const description = document.getElementById('description1');
    const preview = document.getElementById('previewImage1');
    const form = document.getElementById('editProductForm');

    try {
        const res = await fetch(`/inventory/viewproduct/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data)

            if (data.status === 'success') {
                editModal.style.display = "flex";

                subcategory.value = data.subcategory;

                brand.value = data.brand;
                name.value = data.name; 
                
                description.value = data.description;

                if (data.image) {
                    preview.src = data.image; 
                } else {
                    console.log('No image found.');
                }

                for (let option of subcategory.options) {
                    if (option.text === data.subcategory) {
                        option.selected = true;
                        break;
                    }
                }

                for (let option of brand.options) {
                    if (option.text === data.brand) {
                        option.selected = true;
                        break;
                    }
                }

                form.action = `/inventory/editproduct/${id}/`;

                form.onsubmit = async (e) => {
                    e.preventDefault();

                    const formData = new FormData(form);

                    try {
                        const res = await fetch(form.action, {
                            method: 'POST',
                            body: formData,
                        });

                        if (res.ok) {
                            const data = await res.json();

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
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
};

function closeEditModal() {
    document.getElementById('editModal').style.display = 'none';
}
// Product EDIT MODAL   

