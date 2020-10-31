import os
import base64
from Crypto.Cipher import AES
import sys
import getpass
from pathlib import Path
import pickle

def encrypt(key, data, encode=True):
    key = key[:32].zfill(32)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return pickle.dumps((cipher.nonce, tag, ciphertext))

def encrypt_ssh_folder():
    source_path = Path(__file__).parent/".ssh"
    dest_path = Path(__file__).parent/"encrypted.ssh"
    print(f"encrypting {source_path} to {dest_path}")

    password = getpass.getpass().encode('utf-8')
    password2 = getpass.getpass("Confirm Password: ").encode('utf-8')
    if password != password2:
        raise Exception("passwords didnt match")

    files = []
    for file_to_enc in os.listdir(source_path):
        if file_to_enc in ["known_hosts", "authorized_keys"]:
            continue
        with open(source_path/file_to_enc, "r") as handle:
            print("encrypting", file_to_enc)
            file_data = handle.read()
            files.append((file_to_enc, file_data))

    encrypted_files = encrypt(password, pickle.dumps(files))

    with open(dest_path, "wb+") as handle:
        handle.write(encrypted_files)

if __name__ == "__main__":
    encrypt_ssh_folder()
