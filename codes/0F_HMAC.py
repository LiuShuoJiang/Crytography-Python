import hashlib, base64

# Alice and Bob share a secret key

secret_key = "secret key".encode()

# Alice wants to compute a MAC
m = "Hey Bob. How are you?".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
hmac = base64.b64encode(hmac)
print(m, hmac)


# Eve modifies the message
def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


m = modify(m)
print(m)


# Bob receives and validates the HMAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
hmac = base64.b64encode(hmac)
print(m, hmac)
