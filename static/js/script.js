// Automatically submit the form when an image is selected
document.getElementById("file-upload").addEventListener("change", function() {
    document.getElementById("upload-form").submit();
});

// Function to copy HEX code to clipboard
function copyToClipboard(hexCode) {
    if (!hexCode.startsWith("#")) {
        hexCode = "#" + hexCode;  // Ensure the # is included
    }
    
    navigator.clipboard.writeText(hexCode).then(() => {
        alert(`Copied: ${hexCode}`);
    }).catch(err => {
        console.error("Clipboard copy error:", err);
    });
}
