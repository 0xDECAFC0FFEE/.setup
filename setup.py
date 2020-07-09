import os
from zshrc_src import init_zshrc
from ssh import init_ssh, decrypt_ssh_folder
from pathlib import Path

print("downloading submodules")
os.system("git submodule update --init --recursive\\")
submodule_source_file = Path("zshrc_src")/"zsh-autosuggestions"/"zsh-autosuggestions.zsh"
if not submodule_source_file.exists():
    raise Exception("submodule source file not downloaded successfully")

init_zshrc.link_zshrc_file()

decrypt_ssh_folder.decrypt_ssh_folder()

init_ssh.link_ssh_file()