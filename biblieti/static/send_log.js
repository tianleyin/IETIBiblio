function save_log(type, message) {
    // Esta función guarda el log en el localStorage
    var logsString = localStorage.getItem('logs');
    var logs = logsString ? JSON.parse(logsString) : [];

    logs.push({type: type, message: message, current_page: window.location.href}); // Agrega el nuevo log a la lista
    localStorage.setItem('logs', JSON.stringify(logs)); // Guarda la lista actualizada en el localStorage
    //console.log("saved log. Current localstorage: ");
    //console.log(localStorage.getItem("logs"));
}


function check_local_storage() {
    // Esta función recorre los logs almacenados en el localStorage y los envía
    var logsString = localStorage.getItem('logs');
    var logs = logsString ? JSON.parse(logsString) : [];

    //console.log("chek local storage. Current localstorage: ");
    //console.log(localStorage.getItem("logs"));

    logs.forEach(function(log) {
        // Envía cada log al servidor utilizando la función send_log()
        //console.log("sended log: ");
        //console.log(log);
        send_log(log.type, log.message, log.current_page);
    });
    // Limpia el localStorage después de enviar los logs
    localStorage.removeItem('logs');
}


function send_log(type, message, current_page) {
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: '/api/send_log/', // La URL a la que deseas enviar la solicitud POST
        type: 'POST',
        contentType: 'application/json',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: JSON.stringify({
            type: type, // Tipo de log (info, warning, error, fatal)
            message: message, // Mensaje del log
            current_page: current_page
        }),
        success: function(response) {
            console.log('Solicitud exitosa:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error en la solicitud:', error);
        }
    }); 
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Verificar si la cookie comienza con el nombre buscado
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

setInterval(check_local_storage, 5000);
