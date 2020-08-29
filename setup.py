import os
from zshrc_src import init_zshrc
from ssh import init_ssh, decrypt_ssh_folder
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--disable-ssh', help='disable ssh install', action='store_true')
parser.add_argument('--disable-zshrc', help='disable linking zshrc', action='store_true')
parser.add_argument('--disable-fzf', help='disable installing fzf', action='store_true')
args = parser.parse_args()

if not args.disable_zshrc:
    init_zshrc.link_zshrc_file()

if not args.disable_fzf:
    os.system("bash install_scripts/install_fzf.sh")

if not args.disable_ssh:
    decrypt_ssh_folder.decrypt_ssh_folder()
    init_ssh.link_ssh_file()
