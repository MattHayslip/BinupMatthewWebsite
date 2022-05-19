1. <!-- if using windows -->
<!-- Windows You can also use py -3 -m venv .venv -->
python -m venv venv

2. <!-- windows activate venv -->
.\venv\Scripts\activate


1. <!-- if using mac or linux -->
<!-- macOS/Linux You may need to run sudo apt-get install python3-venv first -->
python3 -m venv venv

2. <!-- if using mac or linux mac / linux activate venv -->
source venv/bin/activate

<!-- install all the requirements -->
<!-- can be modified changed or used differently  -->
<!-- same as npm install in node -->
3. pip install -r requirements.txt


<!-- anything bellowe here it's optional -->
<!-- update all packages -->
pip-review --auto

<!-- check package versions to see what needs to be updated or not -->
pip-check 

<!-- windows -->
python -m pip install --upgrade pip

<!-- if using mac or linux mac / linux  -->
python3 -m pip install --upgrade pip


<!-- run the app -->
<!-- mac or linux -->
python3 app.py

<!-- windows -->
python app.py
<!-- run the app -->

<!-- the .gitignore is where everything that it's not going to get uploaded goes to -->


<!-- then create a .env file in the project folder and add these data into it -->
HOST = "0.0.0.0"

<!-- the port can be 90 can be any number -->
PORT = 90 

<!-- if using some sort of email set it up using these -->
MAIL_USERNAME = "your email user name"
MAIL_PASSWORD = "your email password"

<!-- for mysql db usage -->
ip       = "where the mysql is hosted"
db       = "name of the db"
username = "login credentials for the db login"  
password = "login credentials for the db login" 


<!-- different development and production keys -->
secret_key_production = "can be anything. but make it random alpha numeric"
secret_key_dev        = "can be anything. but make it random alpha numeric"