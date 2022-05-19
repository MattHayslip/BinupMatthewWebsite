class Ajax {

    constructor(url) {
        this.url = url;
        this.utility = new util();
    }

    //#region handling the data
    setData(data = {}) {
        if (this.utility.isJson(data)) {
            this.data = data;
        } else {
            return console.log(this.utility.toJSON({ 'data': `${data} is not json format` })); // not in json format
        }
    }

    setDomID(mod_id) { // setting where the get method will show the data with ID
        this.mod_id = mod_id;
    }

    setDomClass(mod_class) { // setting where the get method will show the data with class
        this.mod_class = mod_class;
    }

    setCSRFtoken(token) { // for security
        this.token = token;
    }

    setCSRFAjaxConfig() { // protection against CSRF
        $.ajaxSetup(
            {
                beforeSend: function (xhr, settings) {
                    if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", this.token);
                    }
                }
            }
        );
    }
    //#endregion

    //#region check the browser being used and use the correct ajax method
    get() {
        this.setCSRFAjaxConfig(); // ! may not be needed but better safe than sorry
        this.fetch_get();
    }

    post() {
        this.setCSRFAjaxConfig(); // ! may not be needed but better safe than sorry
        this.fetch_post();
    }

    //#endregion

    //#region fetch get / post
    fetch_get() { // getting data from server
        if (this.mod_id != null) {
            try {
                fetch(this.url)
                    .then(x => x.text())
                    .then(y => document.getElementById(this.mod_id).innerHTML = y);
            } catch (err) {
                console.log(err.message);
            }

        } else if (this.mod_class) {
            try {
                fetch(this.url)
                    .then(x => x.text())
                    .then(y => document.getElementById(this.mod_class).innerHTML = y);
            } catch (err) {
                console.log(err.message);
            }

        } else {
            console.log(`neither id nor class has been set`);
        }
    }

    fetch_post() { // posting data to server
        try {

            fetch(this.url, {

                // Adding method type
                method: "POST",
                mode: 'same-origin',  // Do not send CSRF token to another domain.

                body: JSON.stringify( // JSON format
                    this.data
                ),
                // Adding headers to the request
                headers: {
                    "Content-type": "application/json; charset=UTF-8",
                    'X-CSRFToken': this.token
                }
            })

                // Converting to JSON
                .then(response => response.json())

                // Displaying results to console
                .then(json => console.log(json));

        } catch (err) {
            console.log(err.message);
        }
    }
    //#endregion

    //#region jquery get / post
    get_jquery() {
        if (this.mod_id != null) {
            try {
                $.get(this.url, function (data, status) {
                    $(`#${this.mod_id}`).html(data);
                });
            } catch (err) {
                console.log(err.message);
            }

        } else if (this.mod_class) {
            try {
                $.get(this.url, function (data, status) {
                    $(`#${this.mod_class}`).html(data);
                });
            } catch (err) {
                console.log(err.message);
            }

        } else {
            console.log(`neither id nor class has been set`);
        }
    }

    post_jquery() {
        try {
            $.post(this.url,
                this.data, // json
                function (data, status) {
                    console.log(`Status: ${status}`);
                });
        } catch (err) {
            console.log(err.message);
        }
    }
    //#endregion

    //#region old method get / post
    get_old() {
        if (this.mod_id != null) {
            try {
                const xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById(this.mod_id).innerHTML =
                            this.responseText;
                    }
                };
                xhttp.open("GET", this.url);
                xhttp.send();
            } catch (err) {
                console.log(err.message);
            }

        } else if (this.mod_class) {
            try {
                const xhttp = new XMLHttpRequest();
                xhttp.onreadystatechange = function () {
                    if (this.readyState == 4 && this.status == 200) {
                        document.getElementById(this.mod_class).innerHTML =
                            this.responseText;
                    }
                };
                xhttp.open("GET", this.url);
                xhttp.send();
            } catch (err) {
                console.log(err.message);
            }

        } else {
            console.log(`neither id nor class has been set`);
        }

    }

    post_old() {
        try {
            var xmlhttp = new XMLHttpRequest(); // new HttpRequest instance 
            var theUrl = this.url;

            xmlhttp.open("POST", theUrl);
            xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xmlhttp.send(
                JSON.stringify(this.data)
            );
        } catch (err) {
            console.log(err.message);
        }
    }
    //#endregion

}