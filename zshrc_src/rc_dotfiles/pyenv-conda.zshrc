# manage python, pyenv, anaconda etc install
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init - --no-rehash)"
fi

# looking for conda install location
conda_install_locations=("/usr/local" "/root/berryconda3" "/opt/conda" ~"/.pyenv/versions/anaconda3-2019.07")
for install_location in $conda_install_locations; do; 
    if [ -f $install_location"/bin/conda" ]; then
        conda_dir=$install_location
        break
    fi
done

__conda_setup="$($conda_dir'/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ -v __conda_setup ]; then
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
        add_to_path "$conda_dir/bin"
    else
        if [ -f "$conda_dir/etc/profile.d/conda.sh" ]; then
            . "$conda_dir/etc/profile.d/conda.sh"
        else
            add_to_path "$conda_dir/bin"
        fi
    fi
    unset __conda_setup
fi

if command -v pyenv-virtualenv &>/dev/null; then
    export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    eval "$(pyenv virtualenv-init -)"
fi
