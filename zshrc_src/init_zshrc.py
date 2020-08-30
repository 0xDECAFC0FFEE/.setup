import os
from pathlib import Path
import re

def link_zshrc_file(remove_dest=False):
    zshrc_source = Path(__file__).resolve().parent/".zshrc"
    zshrc_destination = Path().home()/".zshrc"

    if not zshrc_source.exists():
        raise Exception(f".zshrc source file not found")
    if zshrc_destination.exists() and remove_dest:
        os.remove(zshrc_destination)
    elif zshrc_destination.exists():
        raise Exception(f".zshrc file already exists at {zshrc_destination}")

    print(f"symlinking {zshrc_source} to {zshrc_destination}")
    os.system(f"ln -sf {zshrc_source} {zshrc_destination}")

def link_oh_my_zsh_packages():
    # symlinking oh-my-zsh packages in .setup
    os.system("rm -r ~/.oh-my-zsh/plugins")
    print(Path(__file__).resolve().parent/'oh-my-zsh-plugins')
    os.system(f"ln -s {Path(__file__).resolve().parent/'oh-my-zsh-plugins'} ~/.oh-my-zsh/plugins")

def install_oh_my_zsh():
    oh_my_zsh_install_location = os.environ.get("ZSH", False)
    if not oh_my_zsh_install_location or not Path(oh_my_zsh_install_location).exists():
        print("installing oh_my_zsh")
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
    else:
        print("skipping oh-my-zsh install - already detected")

if __name__ == "__main__":
    install_oh_my_zsh()
    link_oh_my_zsh_packages()
    link_zshrc_file(True)
