$(function () {
    var data = JSON.parse(localStorage.getItem('datos'))
    var elementDisplay = ""
    var translatedType = ""
    
    switch (data.type) {
        case "Book":
            translatedType = "Llibre"
            elementDisplay = `<li>${data.name}</li><li>Tipus: ${translatedType}</li><li>Autor/a: ${data.author}</li><li>Any de publicació: ${data.publication_year}</li><li>ISBN: ${data.ISBN}</li>`
            break
        case "CD":
            translatedType = "CD"
            elementDisplay = `<li>${data.name}</li><li>Tipus: ${translatedType}</li><li>Artista: ${data.artist}</li><li>Pistes: ${data.tracks}</li>`
            break
        case "DVD":
            translatedType = "DVD"
            elementDisplay = `<li>${data.name}</li><li>Tipus: ${translatedType}</li><li>Director: ${data.director}</li><li>Duració: ${data.duration}</li>`
            break
        case "BR":
            translatedType = "Blu-Ray"
            elementDisplay = `<li>${data.name}</li><li>Tipus: ${translatedType}</li><li>Resolució: ${data.resolution}</li>`
            break
        case "Device":
            translatedType = "Dispositiu"
            elementDisplay = `<li>${data.name}</li><li>Tipus: ${translatedType}</li><li>Fabricant: ${data.manufacturer}</li><li>Model: ${data.model}</li>`
            break
    }

    $('#element-data').append(elementDisplay)
    $('#id').val(data.id)
})