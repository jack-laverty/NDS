from arinc424 import record
from pymongo import MongoClient, InsertOne
import json
import os

if __name__ == '__main__':
    client = MongoClient('mongodb://192.168.20.3:27017/')
    records = []
    for filename in os.listdir('./input'):
        with open(os.path.join('./input', filename), 'r') as f:
            for line in f.readlines():
                r = record.Record()
                if r.read(line):
                    records.append(InsertOne(json.loads(r.json())))
    print(client.nav_data.dev.bulk_write(records))
    client.close()
