import string
from colorama import init, Fore

# Initialise colorama.
init()


def affine_encrypt(plaintext, a, b):
    # Define the alphabet.
    alphabet = string.ascii_letters
    length_alphabet = len(alphabet)
    ciphertext = ''
    # Iterate through each character in the plaintext.
    for char in plaintext:
        if char in alphabet:
            position = alphabet.index(char)
            # Apply the encryption formula: (a * p + b) mod m.
            encrypt_position = (a * position + b) % length_alphabet
            ciphertext += alphabet[encrypt_position]
        else:
            # If the character is not in the alphabet, keep it unchanged.
            ciphertext += char
    # Return the encrypted ciphertext.
    return ciphertext


# Define the plaintext and key components.
plaintext = input("[?] Enter text to encrypt: ")
a = 9
b = 20
# Call the affine_encrypt function with the specified parameters.
encrypted_text = affine_encrypt(plaintext, a, b)
# Print the original plaintext, the key components, and the encrypted text.
print(f"[+] Plaintext: {plaintext}")
print(f"{Fore.GREEN}[+] Encrypted Text: {encrypted_text}")
