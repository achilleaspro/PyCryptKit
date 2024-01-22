```markdown
# PyCryptKit

PyCryptKit is a Python toolkit for cryptographic operations, offering essential functionalities for encryption and decryption using various algorithms. It is designed to be user-friendly and versatile.

## Features

### 1. Primality Check

- **Function:** `is_prime(n)`
- **Description:** Checks if a given number is prime.

### 2. Miller-Rabin Primality Test

- **Function:** `miller_rabin_primality_test(n, k=5)`
- **Description:** Performs the Miller-Rabin primality test with an optional parameter for accuracy.

### 3. Modular Inverse Function

- **Function:** `mod_inv(a, m)`
- **Description:** Computes the modular inverse of `a` modulo `m`.

### 4. Key Pair Generation

- **Function:** `generate_key_pair(p, q)`
- **Description:** Generates a public-private key pair for encryption and decryption.

### 5. Encryption

- **Function:** `encrypt(pk, plaintext)`
- **Description:** Encrypts plaintext using the public key.

### 6. Decryption

- **Function:** `decrypt(sk, ciphertext)`
- **Description:** Decrypts ciphertext using the private key.

## How to Use

1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/PyCryptKit.git
   cd PyCryptKit
   ```

2. **Run the Script:**
   ```
   python PyCryptKit.py
   ```

3. **Follow the Prompts:**
   - Choose encryption or decryption mode.
   - Select encryption options (plaintext, user-provided keys, or randomly generated keys).

## Example

Suppose you want to encrypt a message. Simply run the script, choose encryption mode, and follow the prompts. You can input your plaintext as an integer or provide prime numbers and an exponent.

## Contribution

Contributions are welcome! If you have ideas for improvement, please submit issues or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```
