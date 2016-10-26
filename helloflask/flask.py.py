from flask import Flask
from flask import send_from_directory

app = Flask(__name__, static_url_path='./introduction/')


@app.route('/')  # Decorator tells Flask what URL should trigger our function
def introduction():
	"""Returns a static page."""
	return send_from_directory('./introduction/', 'index.html')
'''
To actually run this, we need to export the environment variable
"FLASK_APP", ex: export FLASK_APP=hello.py
'''

if __name__ == '__main__':
	app.run()