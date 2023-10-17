const dialogWindow = document.getElementById("feedback-dialog");
const cancelButton = document.getElementById("cancel");

cancelButton.addEventListener("click", (event) => {
  dialogWindow.close();
});
