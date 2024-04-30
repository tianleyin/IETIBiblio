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
            if (response.error) {
                createNotification("error", response.error, $("#user-loans"))
            } else {
                displayLoans(response)
            }
        },
        error: function(xhr, status, error) {
            // Manejar errores aquí
            console.log(error)
        }
    });
}

function displayLoans(response) {
    console.log(response)
    response.forEach(element => {
        var listItemContent = ""

        if (element.catalogue.book) {
            listItemContent += `<ul class="book item" id="${element.id}">
                <li>${element.catalogue.name}</li>
                <li> - Autor/a: ${element.catalogue.book.author}</li>
                <li> - Any de Publicació: ${element.catalogue.book.publication_year} </li>
                <li> - ISBN: ${element.catalogue.book.ISBN}</li>
                <li> - Data de Préstec: ${moment(element.date_of_loan).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li> - Data de Devolució: ${moment(element.date_of_return).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li><button class='return-loan' data='${element.id}'>Marcar Com Retornat</button></li>
            </ul>`
        }
        else if (element.catalogue.cd) {
            listItemContent += `<ul class="cd item" id="${element.id}">
                <li>${element.catalogue.name}</li>
                <li> - Artista: ${element.catalogue.cd.artist}</li>
                <li> - Pistes: ${element.catalogue.cd.tracks} </li>
                <li> - Data de Préstec: ${moment(element.date_of_loan).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li> - Data de Devolució: ${moment(element.date_of_return).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li><button class='return-loan' data='${element.id}'>Marcar Com Retornat</button></li>
            </ul>`
        }
        else if (element.catalogue.dvd) {
            listItemContent += `<ul class="dvd item" id="${element.id}">
                <li>${element.catalogue.name}</li>
                <li> - Director/a: ${element.catalogue.dvd.director}</li>
                <li> - Duració: ${element.catalogue.dvd.duration} minuts</li>
                <li> - Data de Préstec: ${moment(element.date_of_loan).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li> - Data de Devolució: ${moment(element.date_of_return).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li><button class='return-loan' data='${element.id}'>Marcar Com Retornat</button></li>
            </ul>`
        }
        else if (element.catalogue.device) {
            listItemContent += `<ul class="device item" id="${element.id}">
                <li>${element.catalogue.name}</li>
                <li> - Fabricant: ${element.catalogue.device.manufacturer}</li>
                <li> - Model: ${element.catalogue.device.model} </li>
                <li> - Data de Préstec: ${moment(element.date_of_loan).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li> - Data de Devolució: ${moment(element.date_of_return).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li><button class='return-loan' data='${element.id}'>Marcar Com Retornat</button></li>
            </ul>`
        }
        else if (element.catalogue.br) {
            listItemContent += `<ul class="br item" id="${element.id}">
                <li>${element.catalogue.name}</li>
                <li> - Resolució: ${element.catalogue.br.resolution}</li>
                <li> - Data de Préstec: ${moment(element.date_of_loan).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li> - Data de Devolució: ${moment(element.date_of_return).format('YYYY-MM-DD / HH:mm:ss')}</li>
                <li><button class='return-loan' data='${element.id}'>Marcar Com Retornat</button></li>
            </ul>`
        }

        $("#user-loans").append(listItemContent)
    });

    $(".return-loan").click(function (event) {
        event.preventDefault()
        let loanId = $(this).attr('data')
        deleteLoan(loanId)
    })
}

function deleteLoan(loanId) {
    $.ajax({
        url: '/api/delete_loan/',
        type: 'GET', // Método HTTP GET
        data: { id: loanId },
        success: function(response) {
            // Manejar la respuesta exitosa aquí
            $(`#${loanId}`).remove()
            createNotification("info", "Préstec retornat correctament", $("#user-loans"))
        },
        error: function(xhr, status, error) {
            // Manejar errores aquí
            console.error(error);
        }
    });
}