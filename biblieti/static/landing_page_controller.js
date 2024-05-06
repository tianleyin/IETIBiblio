$(function() {
    $("#searchInfo").off().on('input', function() {
        $("#absolute-div ul").empty()
        if ($("#searchInfo").val().length >= 3) {
            let availability = "not-available"
            if ($("#available").is(":checked")) {
                availability = "Available"
            }
            fetch(`/api/get_products_landing/${$("#searchInfo").val()},${availability}`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                let addedNames = []; // Array para almacenar los nombres ya agregados
                for (let i = 0; i < 5; i++) {
                    if (!data[i]) {
                        break
                    }
                    
                    let listItemContent = `<li><span class="catalogue">${data[i].name}</span>`
                    
                    if (data[i].book) {
                        listItemContent += `<ul class="book item">
                            <li> - Autor/a: ${data[i].book.author}</li>
                            <li> - Any de Publicació: ${data[i].book.publication_year} </li>
                            <li> - ISBN: ${data[i].book.ISBN}</li>
                            <li> - CDU: ${data[i].book.CDU}</li> 
                        </ul>`
                    }
                    else if (data[i].cd) {
                        listItemContent += `<ul class="cd item">
                            <li> - Artista: ${data[i].cd.artist}</li>
                            <li> - Pistes: ${data[i].cd.tracks} </li>   
                        </ul>`
                    }
                    else if (data[i].dvd) {
                        listItemContent += `<ul class="dvd item">
                            <li> - Director/a: ${data[i].dvd.director}</li>
                            <li> - Duració: ${data[i].dvd.duration} minuts</li>   
                        </ul>`
                    }
                    else if (data[i].device) {
                        listItemContent += `<ul class="device item">
                            <li> - Fabricant: ${data[i].device.manufacturer}</li>
                            <li> - Model: ${data[i].device.model} </li>   
                        </ul>`
                    }
                    else if (data[i].br) {
                        listItemContent += `<ul class="br item">
                            <li> - Resolució: ${data[i].br.resolution}</li> 
                        </ul>`
                    }
                    
                    listItemContent += `</li>`
                    
                    if (addedNames.indexOf(data[i].name) === -1) {
                        $("#absolute-div > ul").append(listItemContent);
                        addedNames.push(data[i].name);
                    }
                }
            })
        }
    })
})