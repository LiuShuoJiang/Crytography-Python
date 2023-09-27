import hashlib


def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)


m = "This is the hash value message".encode()

m_sha256 = hashlib.sha256()
m_sha256.update(m)
d = m_sha256.digest()

print(d)

m = modify(m)
print(m)

m_sha256 = hashlib.sha256()
m_sha256.update(m)
d = m_sha256.digest()

print(d)
