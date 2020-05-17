import os
from ssh import decrypt_ssh_folder
from pathlib import Path

local_path = Path().home()/".setup"

print(f"symlinking {local_path/'.zshrc'} to ~/.zshrc")
os.system(f"ln -sf {local_path/'.zshrc'} ~/.zshrc")

source_path = local_path/'ssh'/'encrypted.ssh'
dest_path = local_path/'ssh'/'.ssh'
print(f"unencrypting {source_path} to {dest_path}")
decrypt_ssh_folder.decrypt_ssh_folder(source_path, dest_path)

print(f"symlinking {dest_path} to ~/.ssh")
os.system(f"ln -sf {dest_path} ~")
