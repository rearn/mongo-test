from Crypto.Cipher import DES
import pymongo
import json
from binascii import hexlify

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = DES.new("abcdefgh", DES.MODE_ECB)
a = 255
plain = a.to_bytes(8, 'big') 
# 文字数は8の倍数でなければエラーになるのでplainに６文字結合する
ciph = obj.encrypt(plain)
decrypt = obj.decrypt(ciph)
print("plain  :" + hexlify(plain).decode('utf-8'))
print("encrypt:" + hexlify(ciph).decode('utf-8'))
print("decrypt:" + hexlify(decrypt).decode('utf-8'))
client = pymongo.MongoClient('localhost', 27017)
db = client.my_database
co = db.my_collection
co.insert_one(json.dumps({"encrypt": ciph, "decrypt": decrypt}))
for data in co.find():
    print data
