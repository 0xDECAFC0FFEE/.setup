function add_to_path() {
    # if the path exists, add it to $PATH
    if [ -d $1 ]; then
        export PATH=$PATH:$1
    fi
}

if [[ $OSTYPE == "darwin"* ]]; then
    alias ls="ls -Gah"
    alias ip-private="ipconfig getifaddr en0"
    alias new-mac="openssl rand -hex 6 | sed 's/\(..\)/\1:/g; s/.$//' | xargs sudo ifconfig en0 ether"
elif [[ $OSTYPE == "linux-gnu"* ]]; then
    alias ls="ls --color=auto -ah"
    alias nvidia-smi-watch="watch -n0.01 nvidia-smi"
    alias open="xdg-open"
    alias self-control="chomper all 5760"
    alias screenshare="x11vnc -display :1 -noxrecord -noxfixes -noxdamage -forever -passwd fubar"

    alias minecraft-server="tmux-wrap 'sudo ufw reload; cd ~/minecraft_server; java -Xmx1024M -Xms1024M -jar server.jar nogui'; tmux attach"
    alias ip-private="hostname -I | awk '{print \$1}'"

    add_to_path /usr/local/cuda/bin
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    add_to_path ~/.local/bin
    add_to_path /home/$USER/chomper/bin
    export python_version_ROOT="$HOME/.pyenv"
    add_to_path $python_version_ROOT/bin

    bindkey '^[[1;5D' backward-word
    bindkey '^[[1;5C' forward-word

    source ~/.pyenv/completions/pyenv.zsh 2>/dev/null
fi

HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt INC_APPEND_HISTORY
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_SPACE
autoload -Uz compinit && compinit
zstyle ':completion:*' matcher-list '' 'm:{a-zA-Z}={A-Za-z}'
zstyle ':completion:*' menu select
zstyle ':completion:*' completer _complete _correct _approximate 

alias ssh-scai="ssh -tt ucla 'ssh lucas_tong@scai1.cs.ucla.edu -i ~/.ssh/lab'"
alias ssh-scai-tunnel="ssh -L 16006:127.0.0.1:16006 -L 8889:127.0.0.1:8889 -tt ucla 'ssh -L 16006:127.0.0.1:16006 -L 8889:127.0.0.1:8889 lucas_tong@scai1.cs.ucla.edu -i ~/.ssh/lab'"
alias youtube-dl-mp3="youtube-dl --extract-audio --audio-format mp3"
alias youtube-dl="pip install --upgrade youtube-dl; youtube-dl --no-playlist -o '%(title)s.%(ext)s'"
alias glances="glances --fs-free-space"
alias grep="grep -i"
alias ip-public="curl ifconfig.me"

alias tmux-wrap="tmux new-session -d"
alias tmux-jupyter="tmux-wrap 'jupyter lab --no-browser'"
alias tmux-tensorboard="tmux-wrap 'tensorboard --logdir logs'"
alias tmux-tensorboard-pub="tmux-wrap 'tensorboard --logdir logs --host 0.0.0.0'"
alias tmux-env="tmux-jupyter && tmux-tensorboard"
function ssh_tunnel() {
    # creates a tmuxed ssh tunnel from ip address arg1, port arg2 to localhost, port arg3
    tmux-wrap "ssh -L $3:127.0.0.1:$2 $1"
}

source ~/.setup/zshrc_src/ps1_updater/update_ps1_preexec
source ~/.setup/zshrc_src/ps1_updater/bash-preexec.sh
source ~/.setup/zshrc_src/zsh-autosuggestions/zsh-autosuggestions.zsh

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

# fzf
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

