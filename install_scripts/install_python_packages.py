import sys
import subprocess
from pathlib import Path

def install_from_requirements(setup_root_dir: Path):
    """installs packages from requirements.txt"""

    requirements_file_path = setup_root_dir/"requirements.txt"
    print(f"installing packages from {requirements_file_path}")
    
    subprocess.call(f"{sys.executable} -m pip install -r {requirements_file_path}", shell=True)
