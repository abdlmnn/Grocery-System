const formData = {
    product: document.getElementById('product'),
    quantity: document.getElementById('quantity'),
    amountPerUnit: document.getElementById('amountPerUnit'),
    unit: document.getElementById('unit'),
    price: document.getElementById('price'),
    expiryDate: document.getElementById('expiryDate'),
    imagePreview: document.getElementById('imagePreview25'),
};


// Stock ADD MODAL
const openAddModalStock = async () => {

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