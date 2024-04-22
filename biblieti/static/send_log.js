/*class Logs(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    type_choices = [
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('error', 'Error'),
        ('fatal', 'Fatal')
    ]
    type = models.CharField(max_length=20, choices=type_choices)
    client_ip = models.CharField(max_length=255)
    action = models.TextField()
    user_mail = models.EmailField(max_length=255)
    current_page = models.CharField(max_length=255)*/

function send_log(type, message, user_mail) {
    $.ajax({
        url: '/send_log/', // La URL a la que deseas enviar la solicitud POST
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            type: type, // Tipo de log (info, warning, error, fatal)
            message: message, // Mensaje del log
            user_mail: user_mail // Correo electrónico del usuario
        }),
        success: function(response) {
            console.log('Solicitud exitosa:', response);
        },
        error: function(xhr, status, error) {
            console.error('Error en la solicitud:', error);
        }
    }); 
}