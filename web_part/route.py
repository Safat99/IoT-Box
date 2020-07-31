from flask import Flask, render_template,request

from button import button_action

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
@app.route("/dashboard.html")
def dashboard():
	buttons= button_action()
	if buttons.is_submitted():
		# if request.method == 'POST':
		# 	print('HOLA')
		# 	request.form.getlist('mycheckbox') #list er zonno..form er name same thaka lagbo..https://www.youtube.com/watch?v=_sgVt16Q4O4
		print('hello')
		requests=request.form
		relay1=requests.get('Relay1')
		relay2=requests.get('Relay2')
		relay3=requests.get('Relay3')
		relay4=requests.get('Relay4')

		# for showing values>>then upper lines have to commented	
		print(request.form.get('Relay1'))
		print(request.form.get('Relay2'))
		print(request.form.get('Relay3'))
		print(request.form.get('Relay4'))
		# '''


		'''if requests['Relay1']==None:
			print('none')
		else:
			print(requests['Relay1'])'''
		# print(request.form['Relay2'])
		# print(request.form['Relay3'])
		# print(request.form['Relay4'])
		return render_template('dashboard.html',relay1=relay1,relay2=relay2,relay3=relay3,relay4=relay4,temperature =40, humidity = 90)

	return render_template('dashboard.html',temperature =100, humidity = 90)

@app.route("/test.html",methods=['GET','POST'])
def test():
	return render_template('test.html')	
