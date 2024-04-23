$(function () {
    $("a").click(function(event) {
        // Llama a una función específica cuando se hace clic en un enlace
        save_log("info", "Click to redirect");
    });

    $('#btn-logout').click(function(event) {
        save_log("info", "Click to logout");
    });
});