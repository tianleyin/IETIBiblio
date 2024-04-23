$(function() {
    $("#searchInfo").off().on('input', function() {
        $("#absolute-div ul").empty()
        if ($("#searchInfo").val().length >= 3) {
            fetch(`/api/get_products/Any,All,${$("#searchInfo").val()},null,null,null,null,0,null,0,null,null,null`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                for (let i = 0; i < 5; i++) {
                    if (!data[i]) {
                        break
                    }
                    $("#absolute-div ul").append(`<li>${data[i].name}</li>`)
                }
            })
        }
    })
})