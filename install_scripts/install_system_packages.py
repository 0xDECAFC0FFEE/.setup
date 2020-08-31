import sys
import subprocess
from pathlib import Path

def install_ripgrep(platform, install_packages_path):
    print("installing ripgrep")
    if platform == "linux":
        subprocess.call("sudo apt-get install ripgrep", shell=True)
    elif platform == "darwin":
        subprocess.call("brew install ripgrep", shell=True)
    print("installed ripgrep")

def install_fzf(platform, install_packages_path):
    print("installing fzf")

    if not (Path.home()/".fzf").exists():
        subprocess.call(f"git clone --depth 1 https://github.com/junegunn/fzf.git $HOME/.fzf", shell=True)

    subprocess.call("$HOME/.fzf/install --key-bindings --completion --no-update-rc", shell=True)

    print("installed fzf")

def install():
    """
        install useful packages
    """

    install_packages_path = Path(__file__).parent
    platform = sys.platform

    install_fzf(platform, install_packages_path)
    install_ripgrep(platform, install_packages_path)
