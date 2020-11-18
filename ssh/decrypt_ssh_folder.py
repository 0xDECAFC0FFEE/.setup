import base64
import sys
import getpass
from pathlib import Path
import pickle
import os

def decrypt(key, source):
    from Crypto.Cipher import AES
    key = key[:32].zfill(32)
    nonce, tag, ciphertext = pickle.loads(source)
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data

def decrypt_ssh_folder():
    source_path = Path(__file__).parent/"encrypted.ssh"
    dest_path = Path(__file__).parent/".ssh"
    print(f"decrypting {source_path} to {dest_path}")

    password = getpass.getpass().encode('utf-8')

    with open(source_path, "rb") as handle:
        cipherinfo = handle.read()

    try:
        files = pickle.loads(decrypt(password, cipherinfo))
    except:
        raise Exception("password didn't match")

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
