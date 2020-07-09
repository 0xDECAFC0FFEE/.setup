import os
from pathlib import Path

def link_ssh_file():
    ssh_source = Path(__file__).resolve().parent/".ssh"
    ssh_destination = Path().home()/".ssh"

    if not ssh_source.exists():
        raise Exception(f".ssh source folder not found")
    if ssh_destination.exists():
        raise Exception(f".ssh folder already exists at {ssh_destination}")

    print(f"symlinking {ssh_source} to {ssh_destination}")
    os.system(f"ln -sf {ssh_source} {ssh_destination}")

if __name__ == "__main__":
    link_ssh_file()