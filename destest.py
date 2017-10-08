from Crypto.Cipher import DES
import pymongo
import json
from binascii import hexlify

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = DES.new(b'abcdefgh', DES.MODE_ECB)
a = 255
plain = a.to_bytes(8, 'big')
ciph = obj.encrypt(plain)
decrypt = obj.decrypt(ciph)

plain_u   = hexlify(plain).decode('utf-8')
cipj_u    = hexlify(ciph).decode('utf-8')
decrypt_u = hexlify(decrypt).decode('utf-8')

print("plain  :" + plain_u)
print("encrypt:" + cipj_u)
print(ciph)
print("decrypt:" + decrypt_u)
client = pymongo.MongoClient('localhost', 27017, username='test', password='passwd')
db = client.my_database
# db.authenticate('test', 'passwd')
co = db.my_collection
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
