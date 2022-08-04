from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase



firebaseConfig = {
  "apiKey": "AIzaSyBM3Z_lRftI8BI9Pv8q5FgWZjSzszFbPVU",
  "authDomain": "individual-project-faf84.firebaseapp.com",
  "databaseURL": "https://individual-project-faf84-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "individual-project-faf84",
  "storageBucket": "individual-project-faf84.appspot.com",
  "messagingSenderId": "38185549529",
  "appId": "1:38185549529:web:db3926c1732149819888c8",
  "measurementId": "G-TPL435XZFR"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here

@app.route('/signin', methods=['GET', 'POST']) 
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('index'))
		except:
			error = "Authentication failed"
			return error
	else:
		return render_template("signin.html")


@app.route('/signup', methods= ['GET','POST'])
def signup():
	error= ""
	if request. method == 'POST':
		email = request.form ['email']
		password = request. form ['password']
		full_name = request.form ['First_Name']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			user= {"full_name" : full_name, "email": email, "password":password}
			db.child("Users").child(login_session['user']['localId']).set(user)
			return redirect(url_for('homepage'))
		except:
			error = "Authentication failed"
			return error
	else:
		return render_template('signup.html')

@app.route('/index') 
def index():
		return render_template("index.html")

@app.route('/')
def homepage():
	return render_template('home.html')

@app.route('/beauty')
def beautypage():
	return render_template('beauty.html')

@app.route('/bags')
def bagpage():
	return render_template('bags.html')

@app.route('/men')
def menpage():
	return render_template('men.html')

@app.route('/cart')
def cartpage():
	return render_template('Cart.html')

#Code goes above here

if __name__ == '__main__':
	app.run(debug=True)