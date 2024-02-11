# ctec-445-ciphers
# CTEC 445: Fundamentals of Cryptography and Applications - Spring 2024

## Cryptography Python Programs

Welcome to the repository for Python programs related to the "CTEC 445: Fundamentals of Cryptography and Applications" course during the Spring 2024 semester. This repository contains implementations of two classical ciphers: the Caesar cipher and the Affine cipher.

### Table of Contents

1. [Caesar Cipher](#caesar-cipher)
2. [Affine Cipher](#affine-cipher)

---

## Caesar Cipher

The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. The shift value is known as the "key." This cipher is named after Julius Caesar, who is historically known to have used it for secure communication.

### Usage

```bash
python caesar-cipher.py
```
```bash
Would you like to 
 1. Encrypt 
 2. Decrypt
 3. Close
```

## Affine Cipher

The Affine cipher is a more complex substitution cipher that combines the Caesar cipher with modular arithmetic. It encrypts each letter using a mathematical function of the form (ax + b) mod 26, where a and b are the key parameters. The values of a and b must be chosen such that they are coprime with 26.

### Usage

```bash
python affine-cipher.py
```
```bash
[+] Plaintext: <your_input>
[+] Encrypted Text: <encrypted_text>
```
