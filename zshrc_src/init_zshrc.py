import os
from pathlib import Path

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

if __name__ == "__main__":
    link_zshrc_file()