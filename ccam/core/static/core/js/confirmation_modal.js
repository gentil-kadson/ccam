const modalTriggerElements = Array.from(document.querySelectorAll(".confirmation-modal-trigger"));
const modal = document.getElementById("confirmation-modal");
const closeModalButton = document.getElementById("close-modal-button");

modalTriggerElements.forEach(function(trigger) {
    trigger.addEventListener("click", () => modal.showModal());
});

closeModalButton.addEventListener("click", function() {
    modal.close();
});
