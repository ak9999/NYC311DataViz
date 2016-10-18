#!/usr/bin/env python3
import csv
from pymongo import MongoClient

def main():
    # Create MongoClient
    client = MongoClient('localhost', 27017)
    db = client['service_requests']  # Create database.
    db_collection = db['requests']  # Create collection.
    
    with open('/home/akhan/Downloads/data_less_cols.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            db_collection.insert_one(row)
            print(row)

if __name__ == '__main__':
    main()
