from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import sys

def decrypt_file(encrypted_file_path, private_key_path):
    # Load encrypted data
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Load the Private Key
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(key_file.read(), password=None)

    # Decrypt the data
    decrypted_data = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save decrypted file
    decrypted_file_path = encrypted_file_path.replace(".enc", "_decrypted.txt")
    with open(decrypted_file_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"✅ File Decrypted Successfully! 🔓 Saved as: {decrypted_file_path}")

# Run the function (Pass file as command-line argument)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python decrypt_file.py <encrypted_file_path>")
    else:
        decrypt_file(sys.argv[1], "private_key.pem")
