from Crypto.Cipher import DES
from binascii import hexlify

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = DES.new("abcdefgh", DES.MODE_ECB)
a = 255
plain = a.to_bytes(8, 'big') 
# 文字数は8の倍数でなければエラーになるのでplainに６文字結合する
ciph = obj.encrypt(plain)
decrypt = obj.decrypt(ciph)
print("plain  :" + plain.decode('utf-8'))
print("encrypt:" + hexlify(ciph).decode('utf-8'))
print("decrypt:" + decrypt.decode('utf-8'))
