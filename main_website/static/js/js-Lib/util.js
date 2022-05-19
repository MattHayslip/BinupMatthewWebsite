
class util {

    constructor() { // constructor
        // this.notify                 = new Notifications();
        this.chars                  = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
        this.randomStringResult     = "";
    }

    randomString(length) { // generate a random string of alphanumeric characters with length specified
        for (var i = length; i > 0; --i) this.randomStringResult += this.chars[Math.floor(Math.random() * this.chars.length)];
        return this.randomStringResult;
    }

    getRndInteger(min, max) { // generating random integers from min to max
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    randChoice(arr = []) { // choice version from python
        return arr[Math.floor(Math.random() * arr.length)];
    }

    getRndInteger(max) { // generating random integers from min (Default = 1) and max
        return Math.floor(Math.random() * (max - 1 + 1)) + 1;
    }

    rnd() { // generates a random number between 0 and 1
        return Math.random();
    }

    isFloat(num) { // checking if the input is a float
        return Number(num) === n && n % 1 !== 0;
    }

    isInt(num) { // checking if the input is a interger
        return Number.isInteger(num);
    }

    isNumber(num) { // checking if the input is a number
        if (isNaN(num)) {
            return false;
        } else {
            return true;
        }
    }

    isString(str) { // checking if the input is a string
        return typeof str === 'string' || str instanceof String;
    }

    isObject(val) { // checking if the input is an object
        return val instanceof Object;
    }

    isArray(myARR) { // checking if the input is an array type
        return myARR.constructor === Array;
    }

    isDate(myDate) { // checking if the input is date type
        return myDate.constructor === Date;
    }

    isEmpty(data) { // checking if the input is null or not
        return !data.trim().length;
    }

    len(data) { // return the size of the data in INT
        return parseInt(data.length);
    }

    turnInt(data) { // returns value as integer
        return parseInt(data);
    }

    uperCase(str) { // return string in upper case
        return str.toUpperCase();
    }

    lowerCase(str) { // return string in lower case
        return str.toLowerCase();
    }

    toString(data) { // returns data as a string
        return data.toString();
    }

    trim(str) { // trim the empty spaces of a string
        return str.trim();
    }

    isJson(data) { // checking if the input is a JSON or not
        try {
            JSON.parse(data);
        } catch (e) {
            return false;
        }
        return true;
    }

    jsonify(data) { // returns the data as a json object
        return JSON.parse(data);
    }

    replaceWord(main_string, rep_word, rep_with) { // replace the rep_word with rep_with
        return main_string.replace(rep_word, rep_with);
    }

    print(data) { // printing on the console
        console.log(data);
    }

    strSearch(str, searchWord) { // search for specific words (searchWord) in str
        return str.search(searchWord);
    }

    hasVal(str, val) { // returns true if the string contains val 
        return str.includes(val);
    }

    ValidateEmail(mail) { // validate the email to be sure it's in the same format
        if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
            return true
        }
        return false
    }
}

// making getting the date and time easier
class DT {
    constructor() { // starts the Date object to be used in the entire class
        this.d      = new Date();
        this.months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
        this.days   = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    }

    getDayDate() { // converts a date to a more readable format
        return this.d.toDateString();
    }

    getDayDateISO() { // converts a Date object to a string, using the ISO standard format
        return this.d.toISOString()
    }

    getFullYear() { // returning the full year in 4 digit number
        return this.d.getFullYear();
    }

    getMonth() { // get the month 
        return this.months[this.d.getMonth()];
    }

    getDate() { // returns the day of a date as a number (1-31)
        return this.d.getDate();
    }

    getTime12(){ // returning the time in 12 hour format

    }

    getTime24() { // get the time in 24 hour format
        return this.d.getHours + " : " + this.d.getMinutes() + " : " + this.d.getSeconds();
    }

    getDayOfWeek() { // returns the day of the week
        return this.days[this.d.getDay()];
    }
}

class Math {

    constructor(){
        //#region constant math
        this.PI      = Math.PI;      // PI
        this.EULER   = Math.E;       // euler
        this.SQRT2   = Math.SQRT2    // square root of 2
        this.SQRT1_2 = Math.SQRT1_2; // square root of 1/2
        this.LN2     = Math.LN2;     // natural logarithm of 2
        this.LN10    = Math.LN10;    // natural logarithm of 10
        this.LOG2E   = Math.LOG2E;   // base 2 logarithm of E
        this.LOG10E  = Math.LOG10E;  // base 10 logarithm of E
        //#endregion
    }

    round(x){ // Returns x rounded to its nearest integer
        return Math.round(x);
    }

    roundUp(x){ // Returns x rounded up to its nearest integer
        return Math.ceil(x);
    }

    roundDown(x){ // Returns x rounded down to its nearest integer
        return Math.floor(x);	
    }

    trunc(x){ // returns the integer part of x
        return Math.trunc(x)
    }

    mathSign(x){ // Returns x rounded down to its nearest integer
        return Math.sign(x);
    }

    powerOf(a, b){ // returns the value of a to the power of b
        return Math.pow(a,b); 
    }

    squareRoot(x){ // returns the square root of x
        return Math.sqrt(x);
    }

    absoluteValue(x){ //  returns the absolute (positive) value of x
        return Math.abs(x);
    }

    min(data=[]){ // find lowesest in a list
        try{
            return Math.min(data);
        }catch(e){
            return toString(e);
        }
    }

    max(data=[]){ // find highest in a list
        try{
            return Math.max(data);
        }catch(e){
            return toString(e);
        }
    }

    log(x){ // returns The natural logarithm returns the time needed to reach a certain level of growth
        return Math.log(x);
    }

    log2(x){ //  returns the base 2 logarithm of x
        return Math.log2(x);
    }

    log10(x){ // returns the base 10 logarithm of x
        return Math.log10(x);
    }

    //#region advanced Math methods
    cosh(x){ // returns the hyperbolic cosine of a number.
        return Math.cosh(x);
    }

    exp(x){ // returns the value of Ex, where E is Euler's number (approximately 2.7183) and x is the number passed to it.
        return Math.exp(x);
    }

    sinh(x){ // returns the hyperbolic sine of a number
        return Math.sinh(x);
    }

    tangent(x){ // returns the tangent of a number
        return Math.tan(x);
    }

    cubicRoot(x){ // returns the cubic root of a number
        return Math.cbrt(x);
    }

    hyperbolicArctangent(x){ // returns the hyperbolic arctangent of a number
        /*
            Note: If the parameter x is greater than 1, or less than -1, the method will return NaN.
            Note: If the parameter x is 1, the method will return Infinity.
            Note: If the parameter x is -1, the method will return -Infinity.
        */
        return Math.atanh(x);
    }

    atan2(y,x){ // returns the arctangent of the quotient of its arguments, as a numeric value between PI and -PI radians
        /*
            The number returned represents the counterclockwise angle in radians (not degrees) between the positive X axis and the point (x, y).
            Note: With atan2(), the y coordinate is passed as the first argument and the x coordinate is passed as the second argument.
        */
        return Math.atan2(y, x);
    }

    arctangent(x){ // returns the arctangent of a number as a value between - PI/2 and PI/2 radians
        return Math.atan(x);
    }

    asinh(x){ // returns the hyperbolic arcsine of a number
        return Math.asinh(x);
    }

    arcsine(x){ // returns the arcsine of a number as a value between -PI/2 and PI/2 radians
        /*
            Note: If the parameter x is outside the range -1 to 1, the browser will return NaN.
            Tip: 1 will return the value of PI/2. -1 will return the value of -PI/2.
        */
        return Math.asin(x);
    }

    acosh(x){ // returns the hyperbolic arccosine of a number
        // Note: If the parameter x is less than 1, the method will return NaN.
        return Math.acosh(x);
    }

    tanh(x){ // returns the hyperbolic tangent of a number
        return Math.tanh(x);
    }

    acos(x){ //  returns the arccosine of a number as a value value between 0 and PI radians
        /*
            Note: If the parameter x is outside the range -1 to 1, the method will return NaN.
            Tip: -1 will return the value of PI.
        */
        return Math.acos(x);
    }
    //#endregion
}