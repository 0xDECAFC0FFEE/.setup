import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import sys
import getpass
from pathlib import Path
import pickle
import os

def decrypt(key, source, decode=True):
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding

def decrypt_ssh_folder():
    source_path = Path(__file__).parent/"encrypted.ssh"
    dest_path = Path(__file__).parent/".ssh"
    print(f"decrypting {source_path} to {dest_path}")

    password = getpass.getpass().encode('utf-8')
    password2 = getpass.getpass("Confirm Password: ").encode('utf-8')
    if password != password2:
        raise Exception("passwords didnt match")

    with open(source_path, "r") as handle:
        encoded_files = handle.read()

    files = pickle.loads(decrypt(password, encoded_files))

    os.makedirs(dest_path, exist_ok=True)
    os.system(f"chmod 700 {dest_path}")
    for fn, filedata in files:
        if fn in ["known_hosts", "authorized_keys"]:
            print(f"decrypted ssh folder contains {fn} file?")

        try:
            os.remove(filedata)
        except:
            pass
        with open(dest_path/fn, "w+") as handle:
            handle.write(filedata)
            if fn[-4:] == ".pub"  or fn == "config":
                os.system(f"chmod 644 {dest_path/fn}")
            else:
                os.system(f"chmod 600 {dest_path/fn}")

    print(f"decrypted {source_path}")

if __name__ == "__main__":
    decrypt_ssh_folder()
