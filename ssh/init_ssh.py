import os
from pathlib import Path
from ssh.encrypt_ssh_folder import encrypt_ssh_folder
import shutil

def link_ssh_file():
    ssh_source = Path(__file__).resolve().parent/".ssh"
    ssh_destination = Path().home()/".ssh"

    if not ssh_source.exists():
        raise Exception(f".ssh source folder not found")
    if ssh_destination.exists():
        raise Exception(f".ssh folder already exists at {ssh_destination}")

    print(f"symlinking {ssh_source} to {ssh_destination}")
    os.system(f"ln -sf {ssh_source} {ssh_destination}")

def overwrite_ssh():
    """
        deletes encrypted .ssh file.
        moves current filesystem's ~/.ssh into .setup/ssh/.ssh
        encrypts .setup/ssh/.ssh to .setup/ssh/encrypted.ssh
        symlinks .setup/ssh/.ssh to ~/.ssh
    """

    ssh_master_location = (Path(__file__).parent/'.ssh').resolve()
    new_ssh_folder = (Path.home()/".ssh").resolve()

    print(f"overwriting setup's ssh folder with files from {new_ssh_folder}")

    if ssh_master_location.exists():
        shutil.rmtree(str(ssh_master_location))
    shutil.move(str(new_ssh_folder), str(ssh_master_location))

    encrypt_ssh_folder()
    link_ssh_file()

if __name__ == "__main__":
    link_ssh_file()