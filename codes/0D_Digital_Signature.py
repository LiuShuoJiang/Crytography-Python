import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


n = 170171
e = 5
d = 9677

# message that Alice wants to sign and send to Bob
message = "Bob you are awesome".encode()

# Step 1: hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value: ", h)

# Step 2: decrypt the hash value (use secret exponent)
sign = h**d % n

# step 3: send message with signature to Bob
print(message, sign)


# This is Eve modifies the message
message = modify(message)
print(message)


# Bob verifying the signature
# Step 1: calculate the hash value of the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, "big") % n
print("Hash value: ", h)

# Step 2: verify the signature
verification = sign**e % n
print("Verification: ", verification)
