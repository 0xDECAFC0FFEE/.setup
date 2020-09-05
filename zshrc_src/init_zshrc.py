import os
from pathlib import Path
import re
import shutil

def link_zshrc_file(force_link=False):
    zshrc_source = Path(__file__).resolve().parent/".zshrc"
    zshrc_destination = Path().home()/".zshrc"

    if not zshrc_source.exists():
        raise Exception(f".zshrc source file not found")
    if zshrc_destination.exists():
        if force_link:
            old_zshrc_destination = Path().home()/".zshrc_old"
            shutil.move(zshrc_destination, old_zshrc_destination)
            print(f"moved existing ~/.zshrc file to {old_zshrc_destination}")
        else:
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
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh) --unattended --keep-zshrc"')
    else:
        print("skipping oh-my-zsh install - already detected")

if __name__ == "__main__":
    install_oh_my_zsh()
    link_oh_my_zsh_packages()
    link_zshrc_file(True)
