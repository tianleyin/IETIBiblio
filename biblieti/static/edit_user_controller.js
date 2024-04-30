$(() => {
    $('#update-user-data').click((e) => {
        e.preventDefault();
        save_log("info", "Submited form to edit user");
        $('#update-form').submit();
    })
})