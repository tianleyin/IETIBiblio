$(() => {
    $("#expand-header").off().on("click", () => {
        $(".expanding-header").toggleClass("expanded")
    })

    $("#product-type").off().on("change", function () {
        let type = $("#product-type").val()
        switch (type) {
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
})