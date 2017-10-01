from Crypto.Cipher import DES
import pymongo
import json
from binascii import hexlify

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = DES.new("abcdefgh", DES.MODE_ECB)
a = 255
plain = a.to_bytes(8, 'big')
ciph = obj.encrypt(plain)
decrypt = obj.decrypt(ciph)

plain_u   = hexlify(plain).decode('utf-8')
cipj_u    = hexlify(ciph).decode('utf-8')
decrypt_u = hexlify(decrypt).decode('utf-8')

print("plain  :" + plain_u)
print("encrypt:" + cipj_u)
print("decrypt:" + decrypt_u)
client = pymongo.MongoClient('localhost', 27017)
db = client.my_database
co = db.my_collection
ca = db.counters
ret = ca.command({'findandmodify', {'update': {'$inc': { 'seq': 1 }}})
#ca.findAndModify({"_id": "user_id"}, , upsert = True)
co.insert_one({"num": a, "encrypt": cipj_u, "decrypt": decrypt_u})
for data in co.find():
    print(data)

for data in ca.find():
    print(data)
