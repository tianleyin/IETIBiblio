$(() => {
    let productType = "Any"
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
        let availability = "Available"

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
                author = $("#author").val()
                ISBN = $("#ISBN").val()
                publishYear = $("#publish-year").val()
                break
            case "CD":
                artist = $("#artist").val()
                tracks = $("#tracks").val()
                break
            case "DVD":
                director = $("#director").val()
                duration = $("#duration").val()
                break
            case "BR":
                resolution = $("#resolution").val()
                break
            case "Device":
                manufacturer = $("#manufacturer").val()
                model = $("#model").val()
                break
        }
        requestProducts(productName, availability, author, ISBN, publishYear, artist, tracks, director, duration, resolution, manufacturer, model)
    })

    function requestProducts(productName, availability, author, ISBN, publishYear, artist, tracks, director, duration, resolution, manufacturer, model) {
        return new Promise((resolve, reject) => {
            fetch(`/api/get_products/${productType},${availability},${productName},${author},${ISBN},${publishYear},${artist},${tracks},${director},${duration},${resolution},${manufacturer},${model}`)
            .then(response => response.json())
            .then(data => {
                renderProducts(data)
            })
        })
    }

    function renderProducts(data) {
        console.log(data)
        $("#search-results").empty()
        data.forEach(element => {
            let translatedType = ""
            switch (element.type) {
                case "Book":
                    translatedType = "Llibre"
                    break
                case "CD":
                    translatedType = "CD"
                    break
                case "DVD":
                    translatedType = "DVD"
                    break
                case "BR":
                    translatedType = "Blu-Ray"
                    break
                case "Device":
                    translatedType = "Dispositiu"
                    break
            }
            let translatedAvailability = ""
            if (element.available) {
                translatedAvailability = "Disponible"
                $("#search-results").append(`
                <li>
                    <div class="product-card">
                        <h2>${element.name}</h2>
                        <p>${translatedType}</p>
                        <p>${translatedAvailability}</p>
                        <a href="loans/${element.id} class='loan-button'">Prestar</a>
                    </div>
                </li>
                `)
            } else {
                translatedAvailability = "No disponible"
            }
            
        });
        $(".expanding-header").removeClass("expanded")
        
        $("#chevron-container").html(`<svg  xmlns="http://www.w3.org/2000/svg"  width="24"  height="24"  viewBox="0 0 24 24"  fill="none"  stroke="currentColor"  stroke-width="2"  stroke-linecap="round"  stroke-linejoin="round"  class="icon icon-tabler icons-tabler-outline icon-tabler-chevron-down"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6 9l6 6l6 -6" /></svg>`)
    }
})