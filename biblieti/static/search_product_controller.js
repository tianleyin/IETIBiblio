$(() => {
    $("#expand-header").off().on("click", () => {
        $(".expanding-header").toggleClass("expanded")
    })

    $("#product-type").off().on("change", function () {
        let type = $("#product-type").val()
        switch (type) {
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
        }
    })
})