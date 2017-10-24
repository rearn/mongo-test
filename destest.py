from Crypto.Cipher import DES
from binascii import hexlify
import base64

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = DES.new(b'12345678', DES.MODE_ECB)
a = b'1234567890a='
plain = base64.urlsafe_b64decode(a)
ciph = obj.encrypt(plain)
decrypt = obj.decrypt(ciph)

plain_u   = hexlify(plain).decode('utf-8')
cipj_u    = hexlify(ciph).decode('utf-8')
decrypt_u = hexlify(decrypt).decode('utf-8')

print("plain  :" + plain_u)
print("encrypt:" + cipj_u)
print(ciph)
print("decrypt:" + decrypt_u)
