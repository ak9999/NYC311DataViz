#!/usr/bin/env python3

import operator
from pymongo import MongoClient

try:
    client = MongoClient('mongodb://localhost:27017/')
    print('Connection successful.')
except:
    print('Could not connect to MongoDB')
    exit()


db = client.requests  # Database
collection = db.sr    # Collection within database
ctypes = collection.distinct("Complaint Type")

d = dict()
print('Create empty list.')
for s in ctypes:
    data = collection.find({'Complaint Type': s})
    d[str(s)] = data.count()

print('Get sorted representation of dictionary')
sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

for l in sorted_d:
    print('{}'.format(l))
