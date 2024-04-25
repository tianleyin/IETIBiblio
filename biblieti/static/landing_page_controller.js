$(function() {
    $("#searchInfo").off().on('input', function() {
        $("#absolute-div ul").empty()
        if ($("#searchInfo").val().length >= 3) {
            fetch(`/api/get_products_landing/${$("#searchInfo").val()}`)
            .then(response => response.json())
            .then(data => {
                console.log(data)
                for (let i = 0; i < 5; i++) {
                    if (!data[i]) {
                        break
                    }
                    
                    if ($("#absolute-div ul").find('li').length === 0) {
                        $("#absolute-div ul").append(`<li>${data[i].name}</li>`)
                    } else {
                        let isRepeated = false

                        $("#absolute-div ul").find('li').each(function() {
                            if ($(this).text() === data[i].name) {
                                isRepeated = true
                            }
                        })
                        if (!isRepeated) {
                            $("#absolute-div ul").append(`<li>${data[i].name}</li>`)
                        }
                    }
                }
            })
        }
    })
})