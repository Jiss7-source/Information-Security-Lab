from sympy import mod_inverse, gcd

def simple_hash(msg):
    h = 0
    for ch in msg: h = h * 31 + ord(ch)
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

signature = pow(h, d, n)
print("Signature:", signature)

verified = pow(signature, e, n)
print("Verified Hash:", verified)

print("Signature VALID" if verified == h % n else "Signature INVALID")