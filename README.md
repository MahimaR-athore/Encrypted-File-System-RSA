# Encrypted File System Using RSA

## 📌 Project Overview
This project provides a **secure file encryption and decryption system** using the **RSA algorithm in Python**.  
It ensures that sensitive files remain **confidential** by encrypting them with a **public key** and decrypting them with a **private key**.

---

## 🚀 Features
- **RSA Key Pair Generation** (Public & Private Keys)
- **File Encryption** (Using RSA Public Key)
- **File Decryption** (Using RSA Private Key)
- **Ensures Data Privacy** by Preventing Unauthorized Access

---

## 🛠 Technologies Used
- **Programming Language:** Python  
- **Libraries:** `cryptography`  
- **Tools:** VS Code, Git, GitHub  

---

## 📥 Installation & Usage   <-- **ADD THE STEPS HERE**
```sh
# Step 1: Clone This Repository
git clone https://github.com/MahimaR-athore/Encrypted-File-System-RSA.git
cd Encrypted-File-System-RSA

# Step 2: Install Required Libraries
pip install cryptography

# Step 3: Generate RSA Key Pair
python key_generator.py
# Creates `public_key.pem` (for encryption) & `private_key.pem` (for decryption)

# Step 4: Encrypt a File
python encrypt_file.py message.txt
# Creates `message.txt.enc`

# Step 5: Decrypt a File
python decrypt_file.py message.txt.enc
# Restores `message_decrypted.txt`

