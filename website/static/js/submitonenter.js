$(".submit").keyup(function(event) {
    if (event.keyCode === 13) {
        $("#id_of_button").click();
    }
});
