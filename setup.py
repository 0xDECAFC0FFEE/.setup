import os
from zshrc_src import init_zshrc
from ssh import init_ssh, decrypt_ssh_folder
from pathlib import Path

init_zshrc.link_zshrc_file()

os.system("bash install_scripts/install_fzf.sh")

decrypt_ssh_folder.decrypt_ssh_folder()

init_ssh.link_ssh_file()
