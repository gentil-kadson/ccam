const modalTriggerElements = Array.from(document.querySelectorAll(".confirmation-modal-trigger"));
const modal = document.getElementById("confirmation-modal");

modalTriggerElements.forEach(function(trigger) {
    trigger.addEventListener("click", () => modal.showModal());
});
