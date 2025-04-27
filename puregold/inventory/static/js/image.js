
const fileInput = document.getElementById('productImage');
const imagePreview = document.getElementById('imagePreview');

// When a file is selected, display the image preview
fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;

            // Clear any previous content
            imagePreview.innerHTML = '';
            // Append the new image
            imagePreview.appendChild(img);
        };

        reader.readAsDataURL(file);
    } else {
        // No file selected, reset preview
        imagePreview.innerHTML = '<span>No image selected</span>';
    }
});