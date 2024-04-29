$(function () {
    $("#submit").click(function () {
        getLoans($("#email").val());
    })
})

function getLoans(email) {
    $.ajax({
        url: '/api/get_user_loans/',
        type: 'GET', // Método HTTP GET
        data: { email: email },
        success: function(response) {
            // Manejar la respuesta exitosa aquí
            displayLoans(response)
        },
        error: function(xhr, status, error) {
            // Manejar errores aquí
            console.error(error);
        }
    });
}

function displayLoans(response) {
    response.forEach(element => {
        console.log(element.catalogue);
    });

    $("#user-loans").append(`
    <li>${response.catalogue}</li>
    <li>
    `)
    //console.log(response.catalogue)
}