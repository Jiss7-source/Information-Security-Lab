def gcd(a, b):
    while b: a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (e * d) % phi == 1:
            return d

def simple_hash(msg):
    h = 0
    for ch in msg:
        h = (h * 31 + ord(ch))
    return h

p, q = 11, 17
n = p * q
phi = (p-1) * (q-1)

e = 3
while gcd(e, phi) != 1:
    e += 2

d = mod_inverse(e, phi)

msg = input("Enter message: ")
h = simple_hash(msg)
print("Hash:", h)

signature = pow(h, d, n)      # Sign with private key
print("Signature:", signature)

verified = pow(signature, e, n)  # Verify with public key
print("Verified Hash:", verified)

if verified == h % n:
    print("Signature VALID")
else:
    print("Signature INVALID")