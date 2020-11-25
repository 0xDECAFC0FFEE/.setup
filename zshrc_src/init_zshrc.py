import os
from pathlib import Path
import re
import shutil

def link_zshrc_file(force_link=False):
    zshrc_source = Path(__file__).resolve().parent/"rc_dotfiles"/".zshrc"
    zshrc_destination = Path().home()/".zshrc"

    if not zshrc_source.exists():
        raise Exception(f".zshrc source file not found")
    if zshrc_destination.exists():
        if force_link:
            old_zshrc_destination = Path().home()/".zshrc.old"
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
    p10krc_source = Path(__file__).resolve().parent/"rc_dotfiles"/".p10k.zsh"
    p10krc_destination = Path().home()/".p10k.zsh"

    if not p10krc_source.exists():
        raise Exception(f".p10k.zsh source file not found")
    if p10krc_destination.exists():
        if force_link:
            old_p10krc_destination = Path().home()/".p10k.zsh.old"
            shutil.move(p10krc_destination, old_p10krc_destination)
            print(f"moved existing ~/.p10k.zsh file to {old_p10krc_destination}")
        else:
            raise Exception(f".p10k.zsh file already exists at {p10krc_destination}")

    print(f"symlinking {p10krc_source} to {p10krc_destination}")
    os.system(f"ln -sf {p10krc_source} {p10krc_destination}")

def link_tmux_rc_file(force_link=True):
    tmux_rc_source = Path(__file__).resolve().parent/"rc_dotfiles"/".tmux.conf"
    tmux_rc_destination = Path().home()/".tmux.conf"

    if not tmux_rc_source.exists():
        raise Exception(f".tmux.conf source file not found")
    if tmux_rc_destination.exists():
        if force_link:
            old_tmux_rc_destination = Path().home()/".tmux.conf.old"
            shutil.move(tmux_rc_destination, old_tmux_rc_destination)
            print(f"moved existing ~/.tmux.conf file to {old_tmux_rc_destination}")
        else:
            raise Exception(f".tmux.conf file already exists at {tmux_rc_destination}")

    print(f"symlinking {tmux_rc_source} to {tmux_rc_destination}")
    os.system(f"ln -sf {tmux_rc_source} {tmux_rc_destination}")
