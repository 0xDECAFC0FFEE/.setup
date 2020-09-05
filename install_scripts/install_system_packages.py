import sys
import subprocess
from pathlib import Path

install_packages_path = Path(__file__).parent
platform = sys.platform

def exec_if_cmd_doesnt_exist(cmd, to_exec):
    subprocess.call(f"if [ -z `command -v {cmd}` ]; then {to_exec}; else echo '{cmd}' is installed; fi", shell=True)

def install_zsh():
    print("installing zsh")
    if platform == "linux":
        exec_if_cmd_doesnt_exist(cmd="zsh", to_exec="sudo apt install zsh -y")
    elif platform == "darwin":
        exec_if_cmd_doesnt_exist(cmd="zsh", to_exec="brew install zsh")

def install_curl():
    print("installing curl")
    if platform == "linux":
        exec_if_cmd_doesnt_exist(cmd="curl", to_exec="sudo apt install curl -y")
    elif platform == "darwin":
        exec_if_cmd_doesnt_exist(cmd="curl", to_exec="brew install curl")

def install_vim():
    print("installing vim")
    if platform == "linux":
        exec_if_cmd_doesnt_exist(cmd="vim", to_exec="sudo apt install vim -y")
    elif platform == "darwin":
        exec_if_cmd_doesnt_exist(cmd="vim", to_exec="brew install vim")

def install_ripgrep():
    print("installing ripgrep")
    if platform == "linux":
        exec_if_cmd_doesnt_exist(cmd="rg", to_exec="sudo apt-get install ripgrep")
    elif platform == "darwin":
        exec_if_cmd_doesnt_exist(cmd="rg", to_exec="brew install ripgrep")
    print("installed ripgrep")

def install_fzf():
    print("installing fzf")

    if not (Path.home()/".fzf").exists():
        subprocess.call(f"git clone --depth 1 https://github.com/junegunn/fzf.git $HOME/.fzf", shell=True)

    subprocess.call("$HOME/.fzf/install --key-bindings --completion --no-update-rc", shell=True)

    print("installed fzf")