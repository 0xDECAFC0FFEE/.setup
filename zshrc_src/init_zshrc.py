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
    source_plugins = Path(__file__).resolve().parent/'oh-my-zsh-plugins'
    dest_plugins = Path('~/.oh-my-zsh/custom/plugins')
    os.system(f"rm -r {dest_plugins}")
    os.system(f"ln -s {source_plugins} {dest_plugins}")

    # symlinking oh-my-zsh themes
    source_themes = Path(__file__).resolve().parent/'oh-my-zsh-themes'
    dest_themes = Path("~/.oh-my-zsh/custom/themes")
    os.system(f"rm -r {dest_themes}")
    os.system(f"ln -s {source_themes} {dest_themes}")

def install_oh_my_zsh():
    oh_my_zsh_install_location = os.environ.get("ZSH", False)
    if not oh_my_zsh_install_location or not Path(oh_my_zsh_install_location).exists():
        print("installing oh_my_zsh")
        os.system('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh) --unattended --keep-zshrc"')
    else:
        print("skipping oh-my-zsh install - already detected")

def link_p10krc_file(force_link=False):
    p10krc_source = Path(__file__).resolve().parent/".p10k.zsh"
    p10krc_destination = Path().home()/".p10k.zsh"

    if not p10krc_source.exists():
        raise Exception(f".p10k.zsh source file not found")
    if p10krc_destination.exists():
        if force_link:
            old_p10krc_destination = Path().home()/".p10k.zsh"
            shutil.move(p10krc_destination, old_p10krc_destination)
            print(f"moved existing ~/.p10k.zsh file to {old_p10krc_destination}")
        else:
            raise Exception(f".p10k.zsh file already exists at {p10krc_destination}")

    print(f"symlinking {p10krc_source} to {p10krc_destination}")
    os.system(f"ln -sf {p10krc_source} {p10krc_destination}")

if __name__ == "__main__":
    install_oh_my_zsh()
    link_oh_my_zsh_packages()
    link_zshrc_file(True)
