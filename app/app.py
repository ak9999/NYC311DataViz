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
	coordinates = collection.find({column: request_type}, projection) # MongoDB Cursor object, iterable.
	print('Successfully obtained {} coordinates.'.format(coordinates.count()))

	def jsonify(query_result):
		return json_util.dumps({'latlong': query_result})  # Convert query results to json and return

	return Response(jsonify(coordinates), mimetype='application/json')  # Return the result of show_it()


@app.route('/nypd', methods=['GET'])
def GetNYPDResponses():
	'''Returns JSON object of coordinates for each instance responded to by the NYPD.'''
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
	coordinates = collection.find({'Agency': 'NYPD'}, projection) # MongoDB Cursor object, iterable.
	print('Successfully obtained {} coordinates.'.format(coordinates.count()))

	def jsonify(query_result):
		return json_util.dumps({'latlong': query_result})  # Convert query results to json and return

	return Response(jsonify(coordinates), mimetype='application/json')
# Run within virtual environment with python3 app/app.py

if __name__ == '__main__':
	app.run()
