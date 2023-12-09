const fileUploadIconElement = document.querySelectorAll("div.ccam-file-input input");
const fileUploadSvgElement = document.querySelectorAll(".file-upload-icon");
const fileUploadTextContainer = document.querySelectorAll(".file-input-text-container");

fileUploadIconElement.forEach((element, index) => {
    element.addEventListener("change", (event) => {
        const textNode = fileUploadTextContainer[index].childNodes[0]
        textNode.data = "Carregado"
        fileUploadSvgElement[index].innerText = "check_circle"
    })
});
