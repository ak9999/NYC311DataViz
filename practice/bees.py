#!/usr/bin/env python3
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
projection = {'_id': False, 'Latitude': True, 'Longitude': True, 'Descriptor': True, 'Agency': True}  # Properties we want.

coordinates = collection.find({'Complaint Type': 'Harboring Bees/Wasps'}, projection)
print('Successfully obtained {} coordinates.'.format(coordinates.count()))

hc_coords = (40.768890, -73.964789)

# Create empty map zoomed in on Hunter College
bees_map = folium.Map(location=hc_coords, zoom_start=12)

print('Inserting points.')
for each in coordinates:
    if each['Latitude'] and each['Longitude']:
        description = '<p>Responding Agency: {}<br>Description: {}</p>'.format(each['Agency'], each['Descriptor'])
        iframe = folium.element.IFrame(html=description, width=300, height=85)
        popup = folium.Popup(iframe, max_width=300)
        folium.Marker([each['Latitude'], each['Longitude']], popup=popup).add_to(bees_map)

bees_map.save('bees.html')
print('Saved map.')