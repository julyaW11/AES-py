
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import sys

def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    with open(file_path + '.enc', 'wb') as f:
        f.write(iv + ciphertext)

def decrypt_file(file_path, key):
    with open(file_path, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    with open(file_path[:-4], 'wb') as f:
        f.write(plaintext)

def main():
    if len(sys.argv) != 4:
        print("Usage: python (code_name).py <file_path> <key> <encrypt/decrypt>")
        return

    file_path = sys.argv[1]
    key = sys.argv[2].encode('utf-8')
    action = sys.argv[3].lower()

    if len(key) != 16:
        print("Key must be 16 bytes long.")
        return

    if action == 'encrypt':
        encrypt_file(file_path, key)
        print("File encrypted successfully.")
    elif action == 'decrypt':
        decrypt_file(file_path, key)
        print("File decrypted successfully.")
    else:
        print("Invalid action. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()