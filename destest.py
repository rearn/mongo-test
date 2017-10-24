import pymongo


plain_u = 235
cipj_u = 122
decrypt_u = 2334

print(plain_u)
print(cipj_u)
print(decrypt_u)
# client = pymongo.MongoClient('localhost', 27017, username='test', password='passwd')
# client = pymongo.MongoClient('localhost', 27017)
client = pymongo.MongoClient('mongodb://%s:%s@localhost' % ('test', 'passwd'))
db = client.database
db.authenticate('test', 'passwd')
co = db.collection
ca = db.counters
for i in [1, 2, 3, 4]:
    print(i)
    ret = ca.find_and_modify({'id': 'user_id'}, {'$inc': {'seq': 1}})
    print(ret)
co.insert_one({"num": 255, "encrypt": cipj_u, "decrypt": decrypt_u})
for data in co.find():
    print(data)

for data in ca.find():
    print(data)
