from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
@app.route("/dashboard.html")
def dashboard():
	return render_template('dashboard.html',temperature =40, humidity = 90)
	
