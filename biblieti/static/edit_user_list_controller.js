$(() => {
    let cur_page = 1
    let url = new URL(window.location)
    if (url.searchParams) {
        cur_page = url.searchParams.get("page")
    }
    $("#previous-page").click(() => {
        console.log("PREV")
        window.location.href = `/edit_user?page=${parseInt(cur_page) - 1}`;
    })
    $("#next-page").click(() => {
        window.location.href = `/edit_user?page=${parseInt(cur_page) + 1}`;
    })
})