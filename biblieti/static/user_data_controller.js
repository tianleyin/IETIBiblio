$(function () {
    // Logs event listeners
    $("a").click(function(event) {
        event.preventDefault();
        save_log("info", "Click to redirect");
        window.location.href = $(this).attr("href");
    });

    $('btn-logout').click(function(event) {
        save_log("info", "Click to logout");
    });

    $('#update-user-data').click(function(event) {
        event.preventDefault();
        save_log("info", "Submited form to change user data");
        $('#update-form').submit();
    });
});