const assessmentDialog = document.querySelector("#assessment-dialog");
const assessmentDialogCloseButton = document.getElementById("assessment-dialog-cancel");

const assessmentDialogTriggerElements = document.querySelectorAll(".assessment-dialog-trigger");

assessmentDialogCloseButton.addEventListener("click", () => {
    assessmentDialog.close();
})

assessmentDialogTriggerElements.forEach((trigger) => {
    trigger.addEventListener("click", () => {
        assessmentDialog.showModal();
    })
});
