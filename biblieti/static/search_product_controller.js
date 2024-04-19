$(() => {
    $("#expand-header").off().on("click", () => {
        console.log("A")
        $(".expanding-header").toggleClass("expanded")
    })
})