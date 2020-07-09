# to set up a new computer with my creds:
1. `cd ~`
2. `git clone git@github.com:0xDECAFC0FFEE/.setup.git`
3. `pip3 install -r requirements.txt`
4. `python3 setup.py`

# to setup for use in an existing computer:
1. backup .ssh folder and .zshrc file
2. `cd ~; git clone git@github.com:0xDECAFC0FFEE/.setup.git; cd .setup`
3. `pip3 install -r requirements.txt`
4. `cp ~/.ssh ssh`
5. modify zshrc_src/.zshrc with personal .zshrc file
6. `python3 ssh/encrypt_ssh_folder.py`
7. make sure .zshrc and .ssh are backed up
8. `rm ~/.zshrc; rm -r ~/.ssh`
9. `python3 setup.py`