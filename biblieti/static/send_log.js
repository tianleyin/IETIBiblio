function save_log(type, message) {
    // Esta función guarda el log en el localStorage
    var logs = JSON.parse(localStorage.getItem('logs')) || []; // Obtiene los logs almacenados o crea una nueva lista si no hay ninguno
    logs.push({type: type, message: message}); // Agrega el nuevo log a la lista
    localStorage.setItem('logs', JSON.stringify(logs)); // Guarda la lista actualizada en el localStorage
}


function check_local_storage() {
    // Esta función recorre los logs almacenados en el localStorage y los envía
    var logs = JSON.parse(localStorage.getItem('logs')) || []; // Obtiene los logs almacenados o crea una nueva lista si no hay ninguno
    logs.forEach(function(log) {
        // Envía cada log al servidor utilizando la función send_log()
        send_log(log.type, log.message);
    });
    // Limpia el localStorage después de enviar los logs
    localStorage.removeItem('logs');
}


function send_log(type, message) {
    $.ajax({
        url: '/send_log/', // La URL a la que deseas enviar la solicitud POST
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            type: type, // Tipo de log (info, warning, error, fatal)
            message: message // Mensaje del log
        }),
        success: function(response) {
            console.log('Solicitud exitosa:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error en la solicitud:', error);
        }
    }); 
}

setInterval(check_local_storage, 5000);
