$(function () {
    $("#btn-submit-isbn-form").click(function () {
        toggleHidden(true)
        if ($("#isbn").val().trim() === "") {
            createNotification("error", "El camp ISBN no ha d'estar buit")
        } else {
            searchBook($("#isbn").val().trim())
        }
    })

    $("#btn-submit-dinamyc-form").click(function (event) {
        event.preventDefault()
        checkDynamicForm()
    })
})

function searchBook(ISBN) {
    $.ajax({
        url: `/api/search_book_isbn/${ISBN}`,
        dataType: 'json',
        success: function(data) {
          console.log(data)
          fillForm(data)
        },
        error: function(jqXHR, textStatus, errorThrown) {
            createNotification("error", jqXHR.responseJSON.error)
            console.error('error: ', errorThrown)
        }
    })
}

function fillForm(data) {
    toggleHidden(false)
    
    $("#name").val(data.title)
    $("#dynamic-isbn").val($("#isbn").val().trim())
    $("#author").val(data.authors[0])
    $("#publication-year").val(data.published_date.substring(0, 4))
}

function toggleHidden(hide) {
    if (hide) {
        $("#dinamyc-form").hide()
    } else {
        $("#dinamyc-form").show()
    }
}

function checkDynamicForm() {
    let isNameCorrect = feedBackCorrect($("#name"))
    let isIsbnCorrect = feedBackCorrect($("#dynamic-isbn"))
    let isAuthorCorrect = feedBackCorrect($("#author"))
    let isYearCorrect = feedBackCorrect($("#publication-year"))
    let isCduCorrect = feedBackCorrect($("#CDU"))

    if (isNameCorrect && isIsbnCorrect && isAuthorCorrect && isYearCorrect && isCduCorrect) {
        $("#dinamyc-form").submit()
    } else {
        createNotification("error", "Omple tot el formulari correctament")
    }
}

function feedBackCorrect(element) {
    var isCorrect = true
    if (element.val().trim() === "") {
        isCorrect = false
        element.css("border", "2px solid red")
    } else {
        element.css("border", "")
    }
    return isCorrect
}