from install_scripts import install_system_packages
from zshrc_src import init_zshrc
from ssh import init_ssh, decrypt_ssh_folder
from pathlib import Path
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--disable-ssh', help='disable ssh install', action='store_true')
parser.add_argument('--disable-zshrc', help='disable linking zshrc', action='store_true')
parser.add_argument('--overwrite-ssh', help='deletes saved ssh/encrypted.ssh and replaces it with existing ~/.ssh', action='store_true')
parser.add_argument('--disable-system-installs', help='skips installing packages', action='store_true')

args = parser.parse_args()

if not args.disable_system_installs:
    install_system_packages.install_zsh()
    install_system_packages.install_curl()
    install_system_packages.install_vim()
    install_system_packages.install_ripgrep()
    install_system_packages.install_fzf()

if not args.disable_zshrc:
    init_zshrc.install_oh_my_zsh()
    init_zshrc.link_oh_my_zsh_packages()
    init_zshrc.link_zshrc_file(force_link=True)
    init_zshrc.link_p10krc_file(force_link=True)
    init_zshrc.link_tmux_rc_file(force_link=True)

if args.overwrite_ssh:
    init_ssh.overwrite_ssh()
elif not args.disable_ssh:
    decrypt_ssh_folder.decrypt_ssh_folder()
    init_ssh.link_ssh_file(force_link=True)
