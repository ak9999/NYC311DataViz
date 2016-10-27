from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
	"""
	Returns a static page.

	The decorator @app.route('/') tells Flask which URL should trigger our
		function. In this case, '/' is our index.html
	"""
	return render_template('index.html')  # Renders index.html


@app.route('/about')
def about():
    """Returns the about page, which for now is just index.html"""
    return render_template('about.html')


'''
To actually run this, we need to export the environment variable
"FLASK_APP", ex: export FLASK_APP=app.py
'''

if __name__ == '__main__':
	app.run()
