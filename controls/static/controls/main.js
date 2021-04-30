function switchControl(checkbox, controlName) {
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    console.debug("csrftoken: " + csrftoken);
    console.debug("Clicked " + checkbox.id + ", new value = " + checkbox.checked);
    $.ajax({
        method: "PUT",
        url: "/api/controls/1/",
        headers: {'X-CSRFToken': csrftoken},
        data: {
            name: controlName,
            state: checkbox.checked
        }
    })
        .done(function (msg) {
            console.debug(controlName + " set " + checkbox.checked + " in DB successfully");
        })
        .fail(function (jqXHR) {
            console.error("Request failed: " + jqXHR.responseText);
        });
}