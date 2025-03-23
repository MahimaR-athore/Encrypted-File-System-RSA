from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import sys

def encrypt_file(file_path, public_key_path):
    # Read the file data
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Load the Public Key
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(key_file.read())

    # Encrypt Data
    encrypted_data = public_key.encrypt(
        file_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save Encrypted File
    encrypted_file_path = file_path + ".enc"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File Encrypted Successfully! Saved as: {encrypted_file_path}")

# Run the function (Pass file as command-line argument)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encrypt_file.py <file_path>")
    else:
        encrypt_file(sys.argv[1], "public_key.pem")
