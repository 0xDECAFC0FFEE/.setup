import os
from ssh import decrypt_ssh_folder

print("symlinking ~/.startup/.zshrc to ~/.zshrc")
os.system("ln -sf ~/.startup/.zshrc ~/.zshrc")

print("unencrypting ~/.startup/encrypted.ssh to ~/.startup/.ssh")
decrypt_ssh_folder.decrypt_ssh_folder()

print("symlinking ~/.startup/.ssh to .ssh")
os.system("ln -sf ~/.startup/ssh/.ssh ~/.ssh")
