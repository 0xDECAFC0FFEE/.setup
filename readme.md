# to set up a new computer:
1. `git clone git@github.com:0xDECAFC0FFEE/.setup.git ~/.setup`
2. `python3 -m pip install -r ~/.setup/requirements.txt`
3. `python3 ~/.setup/setup.py`

# to setup for use in a computer with existing .ssh and .zshrc:
1. fork .setup
2. backup local .ssh folder and .zshrc file
3. `git clone git@github.com:0xDECAFC0FFEE/.setup.git ~/.setup`
4. update `.setup/zshrc_src/.zshrc` with personal .zshrc info
5. `python3 -m pip install -r ~/.setup/requirements.txt`
6. `python3 ~/.setup/setup.py --overwrite-ssh` # overwrites encryped ssh folder info - you won't need my encryped keys
7. `cd ~/.setup && git add . && git commit -m "updated ssh & zshrc" && git push origin master`
