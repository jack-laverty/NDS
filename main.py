
import arinc424.record as a424
from pymongo import MongoClient, InsertOne
import json

if __name__ == '__main__':
    client = MongoClient('mongodb://192.168.20.3:27017/')
    records = []
    with open('./input/airport') as f:
        for line in f.readlines():
            r = a424.Record()
            if r.validate(line):
                if r.read(line):
                    print(type(json.loads(r.json())))
                    records.append(InsertOne(json.loads(r.json())))
    print('db write:', client.database.collection.bulk_write(records))
    client.close()
