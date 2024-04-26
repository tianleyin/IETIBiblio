$(function () {
    getLoans();
})

function getLoans() {
    $.ajax({
        url: '/api/get_loans/', // La URL a la que deseas enviar la solicitud POST
        type: 'GET',
        contentType: 'application/json',
        success: function(response) {
            console.log('Solicitud exitosa:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error en la solicitud:', error);
        }
    }); 
}