import folium
import pandas as pd
from pymongo import MongoClient
# from IPython.display import display


# Connect to database
try:
    client = MongoClient('mongodb://localhost:27017/')
    print('Connection successful.')
except:
    print('Could not connect to MongoDB')
    exit()

db = client.requests  # Database
collection = db.sr    # Collection within database
projection = {'_id': False, 'Latitude': True, 'Longitude': True, 'Agency': True}  # Properties we want.

# Get the first 'n' coordinates where the responding agency is the NYPD
n = 50
coordinates = collection.find({'Agency': 'NYPD'}, projection)[:n]
print('Successfully obtained coordinates.')

hc_coords = (40.768890, -73.964789)

# Create empty map zoomed in on Hunter College
map_1 = folium.Map(location=hc_coords, zoom_start=12)

print('Inserting points.')
for each in coordinates:
    if each['Latitude'] and each['Longitude']:
        folium.CircleMarker([each['Latitude'], each['Longitude']],
                            radius=1).add_to(map_1)

map_1.save('map1.html')
print('Saved map.')