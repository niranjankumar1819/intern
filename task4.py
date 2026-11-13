from cryptography.fernet import Fernet
import os
import base64
import hashlib
import getpass

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(filename, password):
    try:
        key = generate_key(password)
        fernet = Fernet(key)

        with open(filename, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        with open(filename + ".encrypted", "wb") as file:
            file.write(encrypted_data)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found!")

def decrypt_file(filename, password):
    try:
        key = generate_key(password)
        fernet = Fernet(key)

        with open(filename, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        output_file = filename.replace(".encrypted", ".restored")

        with open(output_file, "wb") as file:
            file.write(decrypted_data)

        print("File decrypted successfully!")
        print("Restored file:", output_file)

    except FileNotFoundError:
        print("File not found!")

    except Exception:
        print("Decryption failed! Check your password or file.")

print("===== FILE PROTECTION UTILITY =====")
print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Enter your choice: ")
filename = input("Enter file name: ")
password = getpass.getpass("Enter password: ")

if choice == "1":
    encrypt_file(filename, password)

elif choice == "2":
    decrypt_file(filename, password)

else:
    print("Invalid choice!")
