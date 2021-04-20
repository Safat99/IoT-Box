from flask import Flask

app = Flask(__name__)

from route import * 
app.config['SECRET_KEY']='12345'


if __name__== '__main__':
	app.run(debug=True)