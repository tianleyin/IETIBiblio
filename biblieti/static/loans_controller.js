$(() => {

    $(".expanding-header").toggleClass('expanded');

    let productType = "Any"
    let availability = "All"
    let productName = "null"
    let author = 'null'
    let ISBN = 'null'
    let publishYear = 'null'
    let artist = 'null'
    let tracks = 0
    let director = 'null'
    let duration = 0
    let resolution = 'null'
    let manufacturer = 'null'
    let model = 'null'
    let page = 1;
    let maxPage = 1;
    let url = new URL(window.location)
    if (url.searchParams && url.searchParams.get("searchInfo")) {
        requestProducts(url.searchParams.get("searchInfo"), "All", "null", "null", "null", "null", 0, "null", 0, "null", "null", "null")
    }
    $("#expand-header").off().on("click", () => {
        $(".expanding-header").toggleClass("expanded")
        if ($(".expanding-header").hasClass("expanded")) {
            $("#chevron-container").html(`<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-chevron-up"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6 15l6 -6l6 6" /></svg>`)
        } else {
            $("#chevron-container").html(`<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-chevron-down"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6 9l6 6l6 -6" /></svg>`)
        }
    })

    $("#product-type").off().on("change", function () {
        productType = $("#product-type").val()
        switch (productType) {
            case "Any":
                $("#dynamic-fieldset").html("")
                break
            case "Book":
                $("#dynamic-fieldset").html(`
                <fieldset>
                    <legend>Filtres avançats</legend>
                    <div class="form-row space-around">
                        <div>
                            <label for="author">Autor</label>
                            <input type="text" id="author" name="author" placeholder="Autor">
                        </div>
                        <div>
                            <label for="ISBN">ISBN</label>
                            <input type="text" id="ISBN" name="ISBN" placeholder="ISBN">
                        </div>
                        <div>
                            <label for="publish-year">Any de publicació</label>
                            <input type="number" id="publish-year" name="publish-year" placeholder="Any de publicació">
                        </div>
                    </div>
                </fieldset>
                `)
                break
            case "CD":
                $("#dynamic-fieldset").html(`
                <fieldset>
                    <legend>Filtres avançats</legend>
                    <div class="form-row space-around">
                        <div>
                            <label for="artist">Artista</label>
                            <input type="text" id="artist" name="artist" placeholder="Artista">
                        </div>
                        <div>
                            <label for="tracks">Nombre de pistes</label>
                            <input type="number" id="tracks" name="tracks" placeholder="Nombre de pistes">
                        </div>
                        <div>
                        </div>
                    </div>
                </fieldset>
                `)
                break
            case "DVD":
                $("#dynamic-fieldset").html(`
                <fieldset>
                    <legend>Filtres avançats</legend>
                    <div class="form-row space-around">
                        <div>
                            <label for="director">Director</label>
                            <input type="text" id="director" name="director" placeholder="Director">
                        </div>
                        <div>
                            <label for="duration">Duració</label>
                            <input type="time" id="duration" name="duration" placeholder="Duració">
                        </div>
                        <div>
                        </div>
                    </div>
                </fieldset>
                `)
                break
            case "BR":
                $("#dynamic-fieldset").html(`
                <fieldset>
                    <legend>Filtres avançats</legend>
                    <div class="form-row space-around">
                        <div>
                            <label for="resolution">Resolució</label>
                            <input type="text" id="resolution" name="resolution" placeholder="Resolution">
                        </div>
                        <div>
                        </div>
                        <div>
                        </div>
                    </div>
                </fieldset>
                `)
                break
            case "Device":
                $("#dynamic-fieldset").html(`
                <fieldset>
                    <legend>Filtres avançats</legend>
                    <div class="form-row space-around">
                        <div>
                            <label for="manufacturer">Manufacturador</label>
                            <input type="text" id="manufacturer" name="manufacturer" placeholder="Manufacturador">
                        </div>
                        <div>
                            <label for="model">Model</label>
                            <input type="text" id="model" name="model" placeholder="Model">
                        </div>
                        <div>
                        </div>
                    </div>
                </fieldset>
                `)
                break
        }
    })

    //$("#reset-filter").off().click(function(e) {
        //createNotification('error', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam feugiat auctor mauris id posuere. Suspendisse sed sodales urna. Sed maximus.')
    //})

    $("#search-button").off().click(function(e) {
        e.preventDefault()
        let productName = $("#product-name").val() == "" ? "null" : $("#product-name").val()
  
        let availability = "not-available"
        if ($("#available").is(":checked")) {
            availability = "Available"
        }

        let author = 'null'
        let ISBN = 'null'
        let publishYear = 'null'
        let artist = 'null'
        let tracks = 0
        let director = 'null'
        let duration = 0
        let resolution = 'null'
        let manufacturer = 'null'
        let model = 'null'
        switch (productType) {
            case "Book":
                author = $("#author").val() == "" ? "null" : $("#author").val()
                ISBN = $("#ISBN").val() == "" ? "null" : $("#ISBN").val()
                publishYear = $("#publish-year").val() == "" ? "null" : $("#publish-year").val()
                break
            case "CD":
                artist = $("#artist").val() == "" ? "null" : $("#artist").val()
                tracks = $("#tracks").val() == "" ? 0 : $("#tracks").val()
                break
            case "DVD":
                director = $("#director").val() == "" ? "null" : $("#director").val()
                duration = $("#duration").val()
                break
            case "BR":
                resolution = $("#resolution").val() == "" ? "null" : $("#resolution").val()
                break
            case "Device":
                manufacturer = $("#manufacturer").val() == "" ? "null" : $("#manufacturer").val()
                model = $("#model").val() == "" ? "null" : $("#model").val()
                break
        }
        requestProducts(productName, availability, author, ISBN, publishYear, artist, tracks, director, duration, resolution, manufacturer, model)
    })

    function requestProducts(productName, availability, author, ISBN, publishYear, artist, tracks, director, duration, resolution, manufacturer, model) {
        if (productName==="null") {
            $("#search-results-title").text("Mostrant tots els Productes");

        } else {
            $("#search-results-title").text('Resultats de la cerca: "' + productName + '"')
        }
        return new Promise((resolve, reject) => {
            fetch(`/api/get_products/${productType},${availability},${productName},${author},${ISBN},${publishYear},${artist},${tracks},${director},${duration},${resolution},${manufacturer},${model},${page}`)
            .then(response => response.json())
            .then(data => {
                maxPage = data.num_pages
                renderProducts(data.data)
            })
        })
    }

    function renderProducts(data) {
        console.log(data)
        $("#search-results").empty()
        data.forEach(element => {
            let translatedType = ""
            let elementData = ""
            switch (element.type) {
                case "Book":
                    translatedType = "Llibre"
                    elementData = `<p>- CDU: ${element.CDU}</p><p>- ISBN: ${element.ISBN}</p><p>- Autor/a: ${element.author}</p><p>- Data de publicació:${element.publication_year}</p>`
                    break
                case "CD":
                    translatedType = "CD"
                    elementData = `<p>- Artista: ${element.artist}</p><p>- Pistes: ${element.tracks}</p>`
                    break
                case "DVD":
                    translatedType = "DVD"
                    elementData = `<p>- Director/a: ${element.director}</p><p>Duració: ${element.duration}</p>`
                    break
                case "BR":
                    translatedType = "Blu-Ray"
                    elementData = `<p>- Resolució: ${element.resolution}</p>`
                    break
                case "Device":
                    translatedType = "Dispositiu"
                    elementData = `<p>- Fabricant: ${element.manufacturer}</p><p>- Model: ${element.model}</p>`
                    break
            }
            var liElement = ""

            if (element.is_same_school && element.state == "Disponible") { // logica de mostrar solamente el boton de prestar en cosas de tu biblioteca y si es disponible
                liElement = `
                <li>
                    <div class="product-card">
                        <h2>${element.name}</h2>
                        <p>- Tipus: ${translatedType}</p>
                        ${elementData}
                        <p>- Estat: ${element.state}</p>
                        <p>- Escola: ${element.school}</p>
                        <a href="/loans_form/" class='loan-button' data='${JSON.stringify(element)}'>Prestar</a>
                    </div>
                </li>`
            } else {
                liElement = `
                <li>
                    <div class="product-card">
                        <h2>${element.name}</h2>
                        <p>- Tipus: ${translatedType}</p>
                        ${elementData}
                        <p>- Estat: ${element.state}</p>
                        <p>- Escola: ${element.school}</p>
                    </div>
                </li>`
            }

            $("#search-results").append(liElement)
            
        });
        if ($("#search-results").children().length === 0) {
            createNotification("info", "No s'han trobat resultats per a la cerca.");
        }
        $(".loan-button").click(function (event) {
            event.preventDefault()
            let datos = $(this).attr('data')
            localStorage.setItem('datos', datos)
            window.location.href = $(this).attr("href")
        })

        $(".expanding-header").removeClass("expanded")
        if (maxPage > 1) {
            $(".pagination-container").removeClass("d-none")
            $("#previous-page").removeClass("disabled")
            $("#next-page").removeClass("disabled")
            if (page === 1) {
                $("#previous-page").addClass("disabled")
            } else if (page === maxPage) {
                $("#next-page").addClass("disabled")
            }
        } else {
            $(".pagination-container").addClass("d-none")
        }
        
        $("#chevron-container").html(`<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-chevron-down"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6 9l6 6l6 -6" /></svg>`)
    }

    $("#next-page").off().click(function() {
        if (page < maxPage) {
            page++
            requestProducts(productName, availability, author, ISBN, publishYear, artist, tracks, director, duration, resolution, manufacturer, model)
            $(window).scrollTop(0)
        }
    })
    $("#previous-page").off().click(function() {
        if (page > 1) {
            page--
            requestProducts(productName, availability, author, ISBN, publishYear, artist, tracks, director, duration, resolution, manufacturer, model)
            $(window).scrollTop(0)
        }
    })
})