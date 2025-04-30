

// Stock EDIT MODAL
const openEditModalStock = async (id) => {
    const formData = {
        // EDIT
        productEdit: document.getElementById('productEdit'),
        quantityEdit: document.getElementById('quantityEdit'),
        amountPerUnitEdit: document.getElementById('amountPerUnitEdit'),
        unitEdit: document.getElementById('unitEdit'),
        priceEdit: document.getElementById('priceEdit'),
        expiryDateEdit: document.getElementById('expiryDateEdit'),
        descriptionEdit: document.getElementById('descriptionEdit'),
        imagePreviewEdit: document.getElementById('previewImage1'),
    };
    
    const editModal = document.getElementById('openEditModalStock');
    const editForm = document.getElementById('editStockForm');
    
    try {
        const res = await fetch(`/inventory/viewstock/${id}/`);

        if (res.ok) {
            const data = await res.json();

            console.log(data);

            if (data.status === 'success') {
                editModal.style.display = 'flex';

                formData.productEdit.value = data.product;
                formData.quantityEdit.value = data.quantity;
                formData.amountPerUnitEdit.value = data.amountPerUnit;
                formData.unitEdit.value = data.unit;
                formData.priceEdit.value = data.price;
                formData.expiryDateEdit.value = data.expiryDate;
                formData.descriptionEdit.value = data.description;

                if (data.image) {
                    formData.imagePreviewEdit.src = data.image;
                } else {
                    console.log('No image found.');
                }

                for (let option of formData.productEdit.options) {
                    if (option.text === data.product) {
                        option.selected = true;
                        break;
                    }
                }

                for (let option of formData.unitEdit.options) {
                    if (option.text == data.unit) {
                        option.selected = true;
                        break;
                    }
                }

                
                formData.productEdit.addEventListener('change', async (e) => {
                    e.preventDefault();
                    const pID = formData.productEdit.value;

                    if (pID) {
                        try {
                            const res = await fetch(`/inventory/getimage/${pID}/`);
            
                            if (res.ok) {
                                const data = await res.json();
            
                                console.log(data);
            
                                if (data.image) {
                                    formData.imagePreviewEdit.src = data.image;
                                } else {
                                    console.log('Message: ', data.message);
                                }
                                    
                            } else {
                                console.log('Error: ', data.message);
                            }
            
                        } catch (error) {
                            console.log('Error: ', error);
                        }
                    } else {
                        console.log('No product id.');
                    }
                });



                editForm.action = `/inventory/editstock/${id}/`;
                // formData.imagePreviewEdit.src = '/media/products/default-noimage.jpg';

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

                            console.log(data);

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
// Stock EDIT MODAL


// Stock VIEW MODAL
const openViewModalStock = async (id) => {
    
    const formData = {
        // VIEW
        productView: document.getElementById('productView'),
        quantityView: document.getElementById('quantityView'),
        amountPerUnitView: document.getElementById('amountPerUnitView'),
        unitView: document.getElementById('unitView'),
        priceView: document.getElementById('priceView'),
        expiryDateView: document.getElementById('expiryDateView'),
        descriptionView: document.getElementById('descriptionView'),
        imagePreviewView: document.getElementById('previewImage'),
    
    };
    const viewModal = document.getElementById('openViewModalStock');
    try {
        const res = await fetch(`/inventory/viewstock/${id}`);

        if (res.ok) {
            const data = await res.json();

            console.log(data);

            if (data.status === 'success') {
                viewModal.style.display = 'flex';

                formData.productView.innerText = data.product;
                formData.quantityView.innerText = data.quantity;

                formData.amountPerUnitView.value = data.amountPerUnit ? data.amountPerUnit : "None";
                formData.unitView.value = data.unit ? data.unit : "None";
                formData.priceView.value = data.price;
                formData.expiryDateView.value = data.expiryDate ? data.expiryDate : "None";
                formData.descriptionView.innerText = data.description;

                if (data.image) {
                    formData.imagePreviewView.src = data.image;
                } else {
                    console.log('No image.');
                }
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
// Stock VIEW MODAL


// Stock ADD MODAL
const openAddModalStock = async () => {

    const formData = {
        // ADD
        product: document.getElementById('product'),
        quantity: document.getElementById('quantity'),
        amountPerUnit: document.getElementById('amountPerUnit'),
        unit: document.getElementById('unit'),
        price: document.getElementById('price'),
        expiryDate: document.getElementById('expiryDate'),
        imagePreview: document.getElementById('imagePreview25'),
    };

    const addForm = document.getElementById('addForm');

    document.getElementById('openAddModalStock').style.display = "flex";
    
    addForm.reset();
    formData.imagePreview.src = '/media/products/default-noimage.jpg';

    formData.product.addEventListener('change', async (e) => {
        e.preventDefault();
        const pID = formData.product.value
        if (pID) {
            try {
                const res = await fetch(`/inventory/getimage/${pID}/`);

                if (res.ok) {
                    const data = await res.json();

                    console.log(data);

                    if (data.image) {
                        formData.imagePreview.src = data.image;
                    } else {
                        console.log('Message: ', data.message);
                    }
                        
                } else {
                    console.log('Error: ', data.message);
                }

            } catch (error) {
                console.log('Error: ', error);
            }
        } else {
            console.log('No product id.');
        }
    });

    // addForm.onsubmit = async (e) => {
    //     e.preventDefault();

    //     const data = new FormData(addForm);

    //     try {
    //         const res = await fetch(`/inventory/addstock/`, {
    //             method: 'POST',
    //             body: data,
    //         });

    //         if (res.ok) {
    //             const data = await res.json();

    //             if (data.status === 'success') {
    //                 console.log('Message', data.message)
    //                 window.location.reload();
    //             } else {
    //                 console.log('Error: ', data.message);
    //             }
    //         } else {
    //             console.log('Something went wrong.')
    //         }
    //     } catch (error) {
    //         console.log('Error: ', error);
    //     }
    // }
};


function closeModal() {
    document.getElementById('openAddModalStock').style.display = 'none';
    document.getElementById('openViewModalStock').style.display = 'none';
    document.getElementById('openEditModalStock').style.display = 'none';
}


window.onclick = function(event) {
    const modals = document.querySelectorAll('.modal-form-container');

    modals.forEach(modal => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
};
// Stock ADD MODAL