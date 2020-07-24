from flask import Flask, render_template

app = Flask(__name__)

@app.route("/dashboard.html")
def dashboard():
	return render_template('dashboard.html')
	#temperature =30, humidity = 90