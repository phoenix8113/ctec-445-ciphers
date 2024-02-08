import string
import secrets


def SelectionScreen():
    choice = int(input("Would you like to \n 1. Encrypt \n 2. Decrypt \n 3. Close \n"))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    elif choice == 3:
        exit()
    else:
        print("Please select a valid option")


def encrypt():
    og_text = input("Enter the text you want to encrypt")
    encryptPass = ''
    for i in og_text:
        if i.isalpha():  # Encrypt letters
            if i.isupper():
                # shifts the character; mod. 26 ensures it stays in the alphabet
                encryptPass += chr((ord(i) + 3 - ord('A')) % 26 + ord('A'))
            else:
                encryptPass += chr((ord(i) + 3 - ord('a')) % 26 + ord('a'))
        elif i.isdigit():  # Encrypt digits
            # shifts the character; mod. 10 ensures it stays in the numbers
            encryptPass += chr((ord(i) + 3 - ord('0')) % 10 + ord('0'))
    print("Original text:", og_text)
    print("Encrypted text:", encryptPass)
    SelectionScreen()


def bruteForceDecrypt(input_text):
    for shift in range(1, 26):
        decrypted_result = ''  # Reset decrypted_result for each shift
        for i in input_text:
            if i.isalpha():
                if i.isupper():
                    decrypted_result += chr((ord(i) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_result += chr((ord(i) - shift - ord('a')) % 26 + ord('a'))
            elif i.isdigit():
                decrypted_result += chr((ord(i) - shift - ord('0')) % 10 + ord('0'))
            else:
                decrypted_result += i

        print("Shift +" + str(shift) + ": " + decrypted_result)
        decrypted_result = ''
    SelectionScreen()


def decrypt():
    encrypted_text = input("Enter encrypted text")
    shift = int(input("Enter the shift (Enter 0 to brute force) "))
    decrypted_result = ''
    if shift != 0:
        for i in encrypted_text:
            if i.isalpha():
                if i.isupper():
                    decrypted_result += chr((ord(i) - shift - ord('A')) % 26 + ord('A'))
                else:
                    decrypted_result += chr((ord(i) - shift - ord('a')) % 26 + ord('a'))
            elif i.isdigit():
                decrypted_result += chr((ord(i) - shift - ord('0')) % 10 + ord('0'))
            else:
                decrypted_result += i
        print(decrypted_result)
        SelectionScreen()
    else:
        bruteForceDecrypt(encrypted_text)

SelectionScreen()