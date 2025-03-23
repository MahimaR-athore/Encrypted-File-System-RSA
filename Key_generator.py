from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generate RSA Key Pair (2048-bit security)
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Standard value used for RSA keys
    key_size=2048  # The key length (higher means stronger security)
)

# Save Private Key to a File
with open("private_key.pem", "wb") as private_file:
    private_file.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,  # Encode as PEM format
            format=serialization.PrivateFormat.PKCS8,  # Standard format for private keys
            encryption_algorithm=serialization.NoEncryption()  # No password protection
        )
    )

# Extract Public Key
public_key = private_key.public_key()

# Save Public Key to a File
with open("public_key.pem", "wb") as public_file:
    public_file.write(
        public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo  # Standard format for public keys
        )
    )
    print("RSA Keys Generated Successfully!")