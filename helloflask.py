from flask import Flask
app = Flask(__name__)

@app.route('/') # Decorator tells Flask what URL should trigger our function
def hello_flask():
	return 'Hello, Flask!'

@app.route('/function')
def yo_flask():
	# some code here to perform a function like return a graph
	return 'Function!'
'''
To actually run this, we need to export the environment variable
"FLASK_APP", ex: export FLASK_APP=hello.py
'''
