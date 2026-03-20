def encrypt(text):
    result=""
    for char in text:
        result+=chr((ord(char)+key-65)%26 +65)
    return result


def decrypt(text):
    result=""
    for char in text:
        result+=chr((ord(char)-65 - key)%26 +65)
    return result

plain_text=input("enter the plaintext:").upper()
key=3
encrypted_text=encrypt(plain_text)

print(f"plain text:{plain_text}")
print(f"encrypted text:{encrypted_text}")
print(f"decrypted text:{decrypt(encrypted_text)}")
