from flask import Flask
from flask import render_template
from flask import Response
from pymongo import MongoClient
from bson import json_util

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

@app.route('/query', methods=['GET'])
@app.route('/query/', methods=['GET'])
@app.route('/query/<request_type>', methods=['GET'])
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
		projection = {'_id': False, 'Latitude': True, 'Longitude': True}  # Properties we want.
		coordinates = collection.find({column: request_type}, projection)
		print('Successfully obtained coordinates.')
		return json_util.dumps({'latlong': coordinates})  # Convert query results to json and return

	return Response(show_it(), mimetype='text/javascript')  # Return the result of show_it()


# Run within virtual environment with python3 app/app.py

if __name__ == '__main__':
	app.run()
