from ensurepip import bootstrap
from flask import Flask,redirect,url_for,render_template,request
from flask_bootstrap import Bootstrap

app=Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('index.html')
    return render_template('index.html')

@app.route('/paradismstrength/coaches')
def ps_coaches():
    pass
@app.route('/paradismstrength/programming')
def ps_programming():
    pass
@app.route('/paradismstrength/contactus')
def ps_contact():
    return "contact"

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)