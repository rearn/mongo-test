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

plain_u   = hexlify(plain).decode('utf-8')
cipj_u    = hexlify(ciph).decode('utf-8')
decrypt_u = hexlify(decrypt).decode('utf-8')

print("plain  :" + plain_u)
print("encrypt:" + cipj_u)
print("decrypt:" + decrypt_u)
client = pymongo.MongoClient('localhost', 27017)
db = client.my_database
co = db.my_collection
co.insert_one(json.dumps({"num": a, "encrypt": cipj_u, "decrypt": decrypt_u}))
for data in co.find():
    print(data)
