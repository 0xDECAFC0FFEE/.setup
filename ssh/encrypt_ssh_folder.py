import os
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import sys
import getpass
import pathlib
import pickle

local_path = pathlib.Path.home()/".startup/ssh"

def encrypt(key, source, encode=True):
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data

password = getpass.getpass().encode('utf-8')
password2 = getpass.getpass("Confirm Password: ").encode('utf-8')
if password != password2:
    raise Exception("passwords didnt match")

files = []
for file_to_enc in os.listdir(local_path/".ssh"):
    if file_to_enc in ["known_hosts", "authorized_keys"]:
        continue
    with open(local_path/".ssh"/file_to_enc, "r") as handle:
        file_data = handle.read()
        print("encrypting", file_to_enc)
        files.append((file_to_enc, file_data))

files = encrypt(password, pickle.dumps(files))

with open(local_path/"encrypted.ssh", "w+") as handle:
    handle.write(files)
