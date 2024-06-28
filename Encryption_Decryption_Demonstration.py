from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, "wb") as key_file:
        key_file.write(key)

def load_key(filename):
    return open(filename, "rb").read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

def save_encrypted_message(encrypted_message, filename):
    with open(filename, "wb") as file:
        file.write(encrypted_message)

def load_encrypted_message(filename):
    return open(filename, "rb").read()

# Main execution
if __name__ == "__main__":
    key_file = "secret.key"
    encrypted_file = "encrypted_message.bin"

    # Generate and save a key
    if not os.path.exists(key_file):
        key = generate_key()
        save_key(key, key_file)
    else:
        key = load_key(key_file)

    # Get a message from the user
    message = input("Enter a message to encrypt: ")

    # Encrypt the message
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")

    # Save the encrypted message to a file
    save_encrypted_message(encrypted_message, encrypted_file)
    print(f"Encrypted message saved to {encrypted_file}")

    # Load the encrypted message from the file
    loaded_encrypted_message = load_encrypted_message(encrypted_file)

    # Decrypt the message
    decrypted_message = decrypt_message(loaded_encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

    # Verify the decryption
    if decrypted_message == message:
        print("Decryption successful! The original message was recovered.")
    else:
        print("Decryption failed. The messages don't match.")