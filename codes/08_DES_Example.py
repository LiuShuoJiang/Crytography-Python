from pyDes import *

message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([1] * 8)
k = des(key, mode=ECB, IV=iv, pad=None, padmode=PAD_PKCS5)

cipher = k.encrypt(message)
print("Length of plain text", len(message))
print("Length of cipher text", len(cipher))
print("encrypted: ", cipher[0:8])
print("encrypted: ", cipher[8:16])
print("encrypted: ", cipher[16:])
message = k.decrypt(cipher)
print("decrypted: ", message)
