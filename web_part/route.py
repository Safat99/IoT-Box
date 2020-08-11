from flask import Flask, render_template,request
import requests
from flask.views import View

from button import button_action

app = Flask(__name__)

class Dashboard(View):
	methods=['GET','POST']
	def __init__(self):
		self.relay1=None
		self.relay2=None
		self.relay3=None
		self.relay4=None
# @app.route("/",methods=['GET','POST'])
# @app.route("/dashboard.html")
	def dispatch_request(self):
		buttons= button_action()
		if buttons.is_submitted():
			# if request.method == 'POST':
			# 	print('HOLA')
			# 	request.form.getlist('mycheckbox') #list er zonno..form er name same thaka lagbo..https://www.youtube.com/watch?v=_sgVt16Q4O4
			print('hello')
			btn=request.form
			self.relay1=btn.get('Relay1')
			self.relay2=btn.get('Relay2')
			self.relay3=btn.get('Relay3')
			self.relay4=btn.get('Relay4')
			# nodemcu = requests.get('http://192.168.1.101/ledon')
			# print(nodemcu.status_code)

			print('hello2')
			# for showing values>>then upper lines have to commented	
			# print(self.relay1)
			# print(type(self.relay1)
			# print(request.form.get('Relay2'))
			# print(request.form.get('Relay3'))
			# print(request.form.get('Relay4'))


			'''if requests['Relay1']==None:
				print('none')
			else:
				print(requests['Relay1'])'''
			# print(request.form['Relay2'])
			# print(request.form['Relay3'])
			# print(request.form['Relay4'])
			return render_template('dashboard.html',relay1=self.relay1,relay2=self.relay2,relay3=self.relay3,relay4=self.relay4,temperature =40, humidity = 90)

		return render_template('dashboard.html',temperature =100, humidity = 90)

	# def getrelay1(self):
	# 	return self.relay1

	# def getrelay2(self):
	# 	return self.relay2

	# def getrelay3(self):
	# 	return self.relay3

	# def getrelay4(self):
	# 	return self.relay4

	# def setrelay1(self,value):
	# 	self.relay1 = value
	# def setrelay2(self,value):
	# 	self.relay2 = value
	# def setrelay3(self,value):
	# 	self.relay3 = value
	# def setrelay4(self,value):
	# 	self.relay4 = value

app.add_url_rule('/',view_func=Dashboard.as_view('dashboard'))

@app.route("/test.html",methods=['GET','POST'])
def test():
	return render_template('test.html')	
