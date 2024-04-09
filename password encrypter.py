
# ----------------------------------------------------------------------------------------------------------------------------------------1st method :

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Example usage:
# Generate and save a key
generate_key()

# Load the key
key = load_key()

# Encrypt a message
encrypted_message = encrypt_message("Hello, World!", key)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted:", decrypted_message)

#----------------------------------------------------------------------------------------------------------------------------------------------------- 2nd method:

import hashlib

def encrypt_password(password):
    # Convert the password to bytes
    password_bytes = password.encode('utf-8')

    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the password bytes
    sha256.update(password_bytes)

    # Get the hexadecimal representation of the digest
    encrypted_password = sha256.hexdigest()

    return encrypted_password

def main():
    password = input("Enter your password: ")
    encrypted_password = encrypt_password(password)
    print("Encrypted Password:", encrypted_password)

if __name__ == "__main__":
    main()
