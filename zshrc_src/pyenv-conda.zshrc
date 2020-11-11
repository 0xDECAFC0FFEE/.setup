# manage python, pyenv, anaconda etc install
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init - --no-rehash)"
fi

if [ -d ~"/.pyenv/versions/anaconda3-2019.07" ]; then # conda location in desktop/pyenv
    conda_dir=~"/.pyenv/versions/anaconda3-2019.07"
elif [ -f "/usr/local/bin/conda" ]; then
    conda_dir="/usr/local"
else
    conda_dir="/opt/conda"
fi

__conda_setup="$($conda_dir'/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "$conda_dir/etc/profile.d/conda.sh" ]; then
        . "$conda_dir/etc/profile.d/conda.sh"
    else
        add_to_path "$conda_dir/bin"
    fi
fi
unset __conda_setup



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
