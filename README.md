# Navigation Data Script
NDS imports ARINC-424 records from text files into a mongoDB database

## Getting Started

* install the following python packages
  * [pymongo](https://pypi.org/project/pymongo/)
  * [arinc424](https://github.com/jack-laverty/arinc424)
* install MongoDB and create a MongoDB database, refer to https://www.mongodb.com/docs/

## Usage

### 1. Update the connection string

edit **main.py** so the MongoClient references your database

```python
client = MongoClient('mongodb://192.168.20.3:27017/') # <-- insert your connection string here
```

You can find your database connection string with **MongoDB Compass**
 
### 2. Add your ARINC-424 records

Gather the files containing your ARINC-424 records and place them inside ```NDS/input``` 

### 3. Run the script

```bash
foo@bar:/src/NDS$ python3 ./main.py
```

After connecting to your server in MongoDB Compass you will find a database called *nav_data* with a collection called *dev* which contains all the ARINC-424 records in JSON format
