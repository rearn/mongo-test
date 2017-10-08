import pymongo


plain_u = 235
cipj_u = 122
decrypt_u = 2334

print(plain_u)
print(cipj_u)
print(decrypt_u)
# client = pymongo.MongoClient('localhost', 27017, username='test', password='passwd')
client = pymongo.MongoClient('localhost', 27017)
db = client.database
db.authenticate('test', 'passwd')
co = db.collection
ca = db.counters
#ca.insert_one({"id": "user_id", 'seq': 0})
for i in [1, 2, 3, 4]:
    print(i)
    ret = ca.find_and_modify({'id': 'user_id'}, {'$inc': { 'seq': 1 }})
    print(ret)
# ret = db.command('findandmodify', 'counters', {'query': {'id': 'user_id'},'update': {$inc: { 'seq': 1 }, 'upsert': True}, 'new': True})
#ca.findAndModify({"_id": "user_id"}, , upsert = True)
co.insert_one({"num": a, "encrypt": cipj_u, "decrypt": decrypt_u})
for data in co.find():
    print(data)

for data in ca.find():
    print(data)
