$(function () {
    // Logs event listeners
    $("a").click(function(event) {
        save_log("info", "Click to redirect");
    });

    $('btn-logout').click(function(event) {
        save_log("info", "Click to logout");
    });

    $('#update-user-data').click(function(event) {
        save_log("info", "Submited form to change user data");
    });
});