const paginationSelect = document.querySelector("select#table-pagination");

paginationSelect.addEventListener("change", triggerEl => {
    const anchorSelector = triggerEl.currentTarget.value;
    const anchorElement = document.getElementById(anchorSelector);
    anchorElement.click();
});
