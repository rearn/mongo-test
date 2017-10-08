import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.database
db.add_user('test', 'passwd', roles=[{'role': "readWrite", 'db': "database"}])
db.counters.insert_one({"id": "user_id", 'seq': 0})
for data in db.counters.find():
    print(data)
