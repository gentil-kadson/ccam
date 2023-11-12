const fileUploadIconElement = document.querySelector("div.ccam-file-input input");
const fileUploadSvgElement = document.getElementById("file-upload-icon");
const fileUploadTextContainer = document.getElementById("file-input-text-container");

fileUploadIconElement.addEventListener("change", (event) => {
    const textNode = fileUploadTextContainer.childNodes[0]
    textNode.data = "Carregado"
    fileUploadSvgElement.innerText = "check_circle"
});
