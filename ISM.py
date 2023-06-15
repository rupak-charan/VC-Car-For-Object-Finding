def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    for i in range(phi):
        if (e * i) % phi == 1:
            return i
    return None

def encrypt(message, e, n):
    ciphertext = []
    for char in message:
        ciphertext.append(pow(ord(char), e, n))
    return ciphertext

def decrypt(ciphertext, d, n):
    message = ""
    for char in ciphertext:
        message += chr(pow(char, d, n))
    return message


def main():
    p = 3
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 3
    if gcd(phi, e) != 1:
        raise Exception("e is not coprime to phi(n)")
    d = modinv(e, phi)
    message = "20BAI1208"
    ciphertext = encrypt(message, e, n)
    decrypted_message = decrypt(ciphertext, d, n)
    print("Message: ", message)
    print("Ciphertext: ", ciphertext)
    print("Decrypted Message: ", decrypted_message)


if __name__ == '__main__':
    main()
