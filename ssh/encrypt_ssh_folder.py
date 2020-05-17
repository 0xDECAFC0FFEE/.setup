import os
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import sys
import getpass
import pathlib
import pickle

def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data

def encrypt_ssh_folder(source_path, dest_path):
    password = getpass.getpass().encode('utf-8')
    password2 = getpass.getpass("Confirm Password: ").encode('utf-8')
    if password != password2:
        raise Exception("passwords didnt match")

    files = []
    for file_to_enc in os.listdir(source_path):
        if file_to_enc in ["known_hosts", "authorized_keys"]:
            continue
        with open(source_path/file_to_enc, "r") as handle:
            file_data = handle.read()
            print("encrypting", file_to_enc)
            files.append((file_to_enc, file_data))

    files = encrypt(password, pickle.dumps(files))

    with open(dest_path, "w+") as handle:
        handle.write(files)

if __name__ == "__main__":
    local_path = pathlib.Path.home()/".setup/ssh"
    source_path = local_path/".ssh"
    dest_path = local_path/"encrypted.ssh"
    encrypt_ssh_folder(source_path, dest_path)
