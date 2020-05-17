# START=`python3 -c 'import time; print(time.time())'`

if [[ $OSTYPE == "darwin"* ]]; then
    alias ls="ls -Gah"
elif [[ $OSTYPE == "linux-gnu"* ]]; then
    alias ls="ls --color=auto -ah"
    alias nvidia-smi-watch="watch -n0.01 nvidia-smi"
    alias open="xdg-open"
    alias self-control="chomper all 5760"
    alias screenshare="x11vnc -display :1 -noxrecord -noxfixes -noxdamage -forever -passwd fubar"

    alias minecraft-server="tmux new-session -d 'sudo ufw reload; cd ~/minecraft_server; java -Xmx1024M -Xms1024M -jar server.jar nogui'; tmux attach"

    export PATH=/usr/local/cuda/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export PATH=~/.local/bin${PATH:+:${PATH}}
    export PATH=$PATH:/home/$USER/chomper/bin
    export python_version_ROOT="$HOME/.pyenv"
    export PATH="$python_version_ROOT/bin:$PATH"

    bindkey '^[[1;5D' backward-word
    bindkey '^[[1;5C' forward-word

    source ~/.pyenv/completions/pyenv.zsh
fi

HISTFILE=~/.zsh_history
HISTSIZE=5000
SAVEHIST=5000
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_SPACE
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' menu select
zstyle ':completion:*' completer _complete _correct _approximate 

alias ssh-scai="ssh -tt ucla 'ssh lucas_tong@scai1.cs.ucla.edu -i ~/.ssh/lab'"
alias tmux-jupyter="tmux new-session -d 'jupyter notebook --no-browser'"
alias youtube-dl-mp3="youtube-dl --extract-audio --audio-format mp3"
alias youtube-dl="pip install --upgrade youtube-dl; youtube-dl --no-playlist"
alias glances="glances --fs-free-space"
alias grep="grep -i"

source ~/.setup/ps1_updater/update_ps1_preexec
source ~/.setup/ps1_updater/bash-preexec.sh

# manage python, pyenv, anaconda etc install
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init - --no-rehash)"
fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!

#! commenting out some conda initialization as its slow as shit and unnecessary
# __conda_setup="$(~'/.pyenv/versions/anaconda3-2019.07/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
# if [ 1 -eq 0 ]; then
#     eval "$__conda_setup"
# else
    if [ -f ~"/.pyenv/versions/anaconda3-2019.07/etc/profile.d/conda.sh" ]; then
        . ~"/.pyenv/versions/anaconda3-2019.07/etc/profile.d/conda.sh"
    else
        export PATH=~"/.pyenv/versions/anaconda3-2019.07/bin:$PATH"
    fi
# fi
# unset __conda_setup
# <<< conda initialize <<<

# use anaconda tf2 environment if in linux and it exists else use base
if [[ $OSTYPE == "linux-gnu"* ]]; then
    conda activate tf2 1>/dev/null 2>&1
fi
if [[ $OSTYPE != "linux-gnu"* || $? == 1 ]]; then
    conda activate base
fi
# echo "zshrc startup time" $((`python3 -c 'import time; print(time.time())'`-$START)) "sec"

if command -v pyenv-virtualenv &>/dev/null; then
    export PYENV_VIRTUALENV_DISABLE_PROMPT=1
    eval "$(pyenv virtualenv-init -)"
fi
