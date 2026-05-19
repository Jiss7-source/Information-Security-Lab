from sympy import mod_inverse, gcd

p=int(input("Enter p value: "))
q=int(input("Enter q value: "))
n = p * q          # 33
phi = (p-1)*(q-1)  # 20

possible_e_values = [e for e in range(2, phi) if gcd(e, phi) == 1]
print(f"Possible values for e (public key exponent): {possible_e_values}")
e = int(input("Enter e value: "))  # public key exponent (coprime with phi)
d = mod_inverse(e, phi)  # private key

print(f"Public Key: ({e}, {n}), Private Key: ({d}, {n})")
M = int(input("Enter numeric value to encrypt: "))
C = pow(M, e, n)   # encrypt
D = pow(C, d, n)   # decrypt

print("\nEncrypted message: ",C)
print("\nDecrypted message: ",D)