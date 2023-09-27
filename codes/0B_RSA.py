import math
import random


def is_prime(p):
    for i in range(2, math.isqrt(p) + 1):
        if p % i == 0:
            return False
    return True


def get_prime(size):
    while True:
        p = random.randrange(size, 2 * size)
        if is_prime(p):
            return p


def lcm(a, b):
    """
    lcm(n) = λ(n) = lcm(λ(p),λ(q)),
    λ(p)=p-1,
    lcm(a,b) = |ab|/gcd(a,b)
    """
    return a * b // math.gcd(a, b)


def get_e(lambda_n):
    """
    Return the smallest integer e such that
    1 < e < λ(n) and gcd(e, λ(n)) = 1
    """
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False


def get_d(e, lambda_n):
    """
    Return the smallest d that solves
    the equation d⋅e ≡ 1 (mod λ(n))
    """
    for d in range(2, lambda_n):
        if d * e % lambda_n == 1:
            return d
    return False


def factor(n):
    for p in range(2, n):
        if n % p == 0:
            return p, n // p


# Key generation by Alice (secret)
# Step 1: generate two distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generate primes: ", p, q)

# Step 2: compute n = p*q
n = p * q
print("Modulus n: ", n)

# Step 3: compute lambda(n)
# (lcm(n) = λ(n) = lcm(λ(p),λ(q)),
# λ(p)=p-1, lcm(a,b) = |ab|/gcd(a,b))
lambda_n = lcm(p - 1, q - 1)
print("Lambda n: ", lambda_n)

# Step 4: choose an integer e
# such that 1 < e < λ(n) and gcd(e, λ(n)) = 1
e = get_e(lambda_n)
print("Public exponent: ", e)

# Step 5: solve for d the equation d⋅e ≡ 1 (mod λ(n)
d = get_d(e, lambda_n)
print("Secret exponent: ", d)

# Done with key generation
print("Public key (e, n): ", e, n)
print("Secret key (d): ", d)


# This is Bob trying to send message
m_bob = 117  # let Bob send the message m_bob = 117 to Alice
c = m_bob**e % n  # Bob should encrypt it with Alice public key and assign it to c.
print("Bod sends: ", c)


# This is Alice decrypting the cipher
m = (
    c**d % n
)  # Alice should decrypt it with her secret key and assign the result to m_alice.
print("Alice message: ", m)


# This is Eve
print("Eve sees the following:")
print("  Public key (e, n) ", e, n)
print("  Encrypted cipher ", c)
p, q = factor(n)
print("Factors: ", p, q)

lambda_n = lcm(p - 1, q - 1)
print("Eve Lambda n: ", lambda_n)

d = get_d(e, lambda_n)
print("Eve Secret exponent: ", d)

m = c**d % n
print("Eve message: ", m)


# This is Bob not being careful
print("This is Bob not being careful")
message = "Alice is awesome"
# He sends the message encrypted letter by letter.
for m_c in message:
    c = ord(m_c)**e % n
    print(c, ' ', end='')
print()
