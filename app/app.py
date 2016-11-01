from flask import Flask
from flask import render_template
from flask import Response
from pymongo import MongoClient

app = Flask(__name__)


@app.route('/')
@app.route('/index.html')
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

@app.route('/query')
@app.route('/query/')
@app.route('/query/<request_type>')
def query(column='Complaint Type', request_type='Special Enforcement'):
	'''Returns Latitude and Longitude of issues.'''
	def show_it():
		# Connect to database
		try:
			client = MongoClient('mongodb://localhost:27017/')
			print('Connection successful.')
		except:
			print('Could not connect to MongoDB')
			return


		db = client.requests  # Database
		collection = db.sr    # Collection within database

		projection = {'_id': False, 'Latitude': True, 'Longitude': True}

		# pymongo's 'find' returns a Cursor object that must be iterated over.
		for x in collection.find({column: request_type}, projection)[:5000]:
			yield '{}<br>\n'.format(x)

	return Response(show_it(), mimetype='text/html')

'''
To actually run this, we need to export the environment variable
"FLASK_APP", ex: export FLASK_APP=app.py
Or just python3 app/app.py
'''

if __name__ == '__main__':
	app.run()
