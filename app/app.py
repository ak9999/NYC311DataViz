from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')  # Decorator tells Flask what URL should trigger our function
def index():
	"""Returns a static page."""
	return render_template('index.html')
'''
To actually run this, we need to export the environment variable
"FLASK_APP", ex: export FLASK_APP=hello.py
'''

if __name__ == '__main__':
	app.run()
