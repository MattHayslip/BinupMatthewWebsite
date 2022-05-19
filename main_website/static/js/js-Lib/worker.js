class Worker {
    constructor() {
        this.w = w;
    }

    set_worker(worker) { // only pass js files
        if (typeof (w) == "undefined") {
            this.w = new Worker(`${worker}`);
        }
    }

    stop() {
        try{
            this.w.terminate();
            this.w = undefined;
        }catch(err){
            console.log(err.message);
        }
    }

    update(id_dom) { // maybe. maybe not :-/
        try{
            w.onmessage = function (event) {
                document.getElementById(id_dom).innerHTML = event.data;
                };
        }catch(err){
            console.log(err.message);
        }
    }
}