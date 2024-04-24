$(function () {
    // Logs event listeners
    $("a").click(function(event) {
        event.preventDefault();
        save_log("info", "Click to redirect to " + $(this).attr("href"));
        window.location.href = $(this).attr("href");
    });

    $('#btn-logout').click(function(event) {
        save_log("info", "Click to logout");
    });
});