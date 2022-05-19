class Lstore {
    setData(data) {
        this.data = data;
    }

    setTitle(title) {
        this.title = title;
    }

    save() { // save the data 
        try {
            localStorage.setItem(this.title, this.data);
        } catch (err) {
            console.log(err);
        }
    }

    get_saved() { // get the saved data
        try {
            return localStorage.getItem(this.title);
        } catch (err) {
            console.log(err);
        }
    }
}

// extends lstore because the title could be the same :-) 
class Cookie extends Lstore {
    setCName(cname) {
        this.cname = cname;
    }

    setCValue(cvalue) {
        this.cvalue = cvalue;
    }

    setExperationDay(exdays) {
        this.exdays = exdays;
    }

    setCookie() {
        try {
            const d = new Date();
            d.setTime(d.getTime() + (this.exdays * 24 * 60 * 60 * 1000));
            let expires = "expires=" + d.toUTCString();
            document.cookie = `${this.cname}=${this.cvalue};${expires};path=/`;
        } catch (err) {
            return err.message;
        }
    }

    getCookie(cname) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, cname.length + 1) === (cname + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(cname.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}