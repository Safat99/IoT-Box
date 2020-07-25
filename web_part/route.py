from flask import Flask, render_template,request

from button import button_action

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@app.route("/dashboard.html")
def dashboard():
	buttons= button_action()
	if buttons.is_submitted():
	# if request == 'POST':
		# request.form.getlist('mycheckbox') //list er zonno
		print('hello')
		print(request.form.get('Relay1'))
		print(request.form.get('Relay2'))
		print(request.form.get('Relay3'))
		print(request.form.get('Relay4'))
		# print(request.form['Relay2'])
		# print(request.form['Relay3'])
		# print(request.form['Relay4'])
				
	return render_template('dashboard.html',temperature =40, humidity = 90)

@app.route("/test.html",methods=['GET','POST'])
def test():
	return render_template('test.html')	
