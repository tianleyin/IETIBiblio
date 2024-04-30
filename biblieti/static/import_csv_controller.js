$(() => {
    $("#import-csv").on("click", (e) => {
        e.preventDefault();
        save_log("info", "Submited form to import csv");
        $("#import-form").submit();
    })
})