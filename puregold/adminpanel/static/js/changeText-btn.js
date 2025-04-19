const changeButtonText = (buttonId, loadingText) => {
    const button = document.getElementById(buttonId);
    const originalText = button.innerText;
    const form = button.closest('.form');  

    if (!form.checkValidity()) {
        return;
    } else {
        button.innerText = loadingText;
        // button.disabled = true;

        setTimeout(() => {
            button.innerText = originalText;    
            button.disabled = false;
        }, 4000);
    }
}

