$(() => {
    $('#add-user-button').click((e) => {
        e.preventDefault();
        save_log("info", "Submited form to add user");
        $('#create-form').submit();
    })
})