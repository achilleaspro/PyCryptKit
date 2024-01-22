import random
from math import gcd

# Check if a given number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Miller-Rabin primality test
def miller_rabin_primality_test(n, k=5):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Modular inverse function
def mod_inv(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

# Generate a key pair for encryption and decryption
def generate_key_pair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)

    d = mod_inv(e, phi)
    return ((e, n), (d, n))

# Encrypt the plaintext using the public key
def encrypt(pk, plaintext):
    e, n = pk
    return [pow(ord(char), e, n) for char in plaintext]

# Decrypt the ciphertext using the private key
def decrypt(sk, ciphertext):
    d, n = sk
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

def main():
    mode = int(input("Enter 1 for encryption or 2 for decryption: "))
    if mode == 1:
        encryption_mode = int(input("Enter encryption mode:\n"
                                     "1: Plaintext as an integer\n"
                                     "2: User-provided p, q, and e\n"
                                     "3: Randomly generated p, q, and e\n"
                                     "Choose option (1, 2, or 3): "))
        if encryption_mode == 1:
            plaintext = input("Enter plaintext as an integer: ")
            e, n, phi = None, None, None
            while True:
                p = random.randint(100, 1000)
                q = random.randint(100, 1000)
                if miller_rabin_primality_test(p) and miller_rabin_primality_test(q):
                    break

            while True:
                e = random.randint(2, 1000)
                n = p * q
                phi = (p - 1) * (q - 1)
                if gcd(e, phi) == 1:
                    break

            print("Generated p:", p)
            print("Generated q:", q)
            print("Generated e:", e)
        else:
            plaintext = input("Enter plaintext (UPPER CASE LETTERS ONLY): ")

        if encryption_mode == 2:
            p = int(input("Enter a prime number p: "))
            q = int(input("Enter a prime number q: "))
            e = int(input("Enter an exponent e: "))
            
            if not (is_prime(p) and is_prime(q)):
                print("p and q must be prime numbers.")
                return

            n = p * q
            phi = (p - 1) * (q - 1)

            if gcd(e, phi) != 1:
                print("e must be relatively prime to (p-1)*(q-1).")
                return

        elif encryption_mode == 3:
            while True:
                p = random.randint(100, 1000)
                q = random.randint(100, 1000)
                if miller_rabin_primality_test(p) and miller_rabin_primality_test(q):
                    break

            e, n, phi = None, None, None
            while True:
                e = random.randint(2, 1000)
                n = p * q
                phi = (p - 1) * (q - 1)
                if gcd(e, phi) == 1:
                    break

            print("Generated p:", p)
            print("Generated q:", q)
            print("Generated e:", e)

        public_key = (e, n)
        encrypted_msg = encrypt(public_key, plaintext)
        print("Encrypted message (numeric):", encrypted_msg)
        encrypted_str = ''.join([chr(x) for x in encrypted_msg])
        print("Encrypted message (string):", encrypted_str)

    elif mode == 2:
        p = int(input("Enter a prime number p: "))
        q = int(input("Enter a prime number q: "))
        e = int(input("Enter an exponent e: "))
        ciphertext = input("Enter ciphertext (UPPER CASE LETTERS ONLY): ")

        if not (is_prime(p) and is_prime(q)):
            print("p and q must be prime numbers.")
            return

        n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(e, phi) != 1:
            print("e must be relatively prime to (p-1)*(q-1).")
            return

        d = mod_inv(e, phi)
        print("Generated d:", d)
        private_key = (d, n)
        decrypted_msg = decrypt(private_key, [ord(x) for x in ciphertext])
        print("Decrypted message (numeric):", [ord(x) for x in decrypted_msg])
        print("Decrypted message (string):", decrypted_msg)

# Run the main function
if __name__ == "__main__":
    main()


