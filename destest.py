from Crypto.Cipher import DES

# "abcdefgh" がキーになる(キーは8バイトの長さでなければならない)
obj = DES.new("abcdefgh", DES.MODE_ECB)
plain = "Guido van Rossum is a space alien."
# 文字数は8の倍数でなければエラーになるのでplainに６文字結合する
ciph = obj.encrypt(plain + "XXXXXX")
decrypt = obj.decrypt(ciph)
print("plain  :" + plain)
print("encrypt:" + ciph)
print("decrypt:" + decrypt)
assert plain = decrypt, "error"
