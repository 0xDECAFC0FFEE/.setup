from pathlib import Path
setup_path = Path(__file__).parent

from install_scripts import install_python_packages
install_python_packages.install_from_requirements(setup_path)

from zshrc_src import init_zshrc
from ssh import init_ssh, decrypt_ssh_folder
from pathlib import Path
import argparse
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--disable-ssh', help='disable ssh install', action='store_true')
parser.add_argument('--disable-zshrc', help='disable linking zshrc', action='store_true')
parser.add_argument('--force-zshrc', help='force .zshrc symlink even if already exists', action='store_true')
parser.add_argument('--disable-fzf', help='disable fzf install', action='store_true')
parser.add_argument('--overwrite-ssh', help='deletes saved ssh/encrypted.ssh and replaces it with existing ~/.ssh', action='store_true')

args = parser.parse_args()

if not args.disable_zshrc:
    init_zshrc.install_oh_my_zsh()
    init_zshrc.link_oh_my_zsh_packages()
    init_zshrc.link_zshrc_file(remove_dest=args.force_zshrc)

if not args.disable_fzf:
    subprocess.call(f"bash {setup_path/'install_scripts'/'install_fzf.sh'}", shell=True)

if args.overwrite_ssh:
    init_ssh.overwrite_ssh()
elif not args.disable_ssh:
    decrypt_ssh_folder.decrypt_ssh_folder()
    init_ssh.link_ssh_file()
