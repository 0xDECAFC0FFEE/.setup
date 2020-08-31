# manage python, pyenv, anaconda etc install
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init - --no-rehash)"
fi

#! commenting out some conda initialization as its slow as shit and unnecessary
if command -v which conda &> /dev/null; then
    if [ -f ~"/.pyenv/versions/anaconda3-2019.07/etc/profile.d/conda.sh" ]; then
        . ~"/.pyenv/versions/anaconda3-2019.07/etc/profile.d/conda.sh"
    else
        add_to_path ~/.pyenv/versions/anaconda3-2019.07/bin
    fi
fi

# use anaconda tf2 environment if in linux and it exists else use base
if [[ $OSTYPE == "linux-gnu"* ]]; then
    conda activate tf2 1>/dev/null 2>&1
fi
if [[ $OSTYPE != "linux-gnu"* || $? == 1 ]]; then
    conda activate base
fi

if command -v pyenv-virtualenv &>/dev/null; then
    export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    eval "$(pyenv virtualenv-init -)"
fi