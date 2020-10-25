export SETUP_DIR=$HOME/.setup

plugins=(git fzf-docker ripgrep fzf-tab fzf-git zsh-autosuggestions)
export ZSH=$HOME/.oh-my-zsh
source $ZSH/oh-my-zsh.sh

function add_to_path() {
    # if the path exists, add it to $PATH
    if [ -d $1 ]; then
        export PATH=$PATH:$1
    fi
}

if [[ $OSTYPE == "darwin"* ]]; then
    add_to_path "$XDG_CONFIG_HOME/nvim/plugged/fzf-wordnet.vim/bin"
elif [[ $OSTYPE == "linux-gnu"* ]]; then
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

function ssh_tunnel() {
    # creates a tmuxed ssh tunnel from ip address arg1, port arg2 to localhost, port arg3
    tmux-wrap "ssh -L $3:127.0.0.1:$2 $1"
}

source $SETUP_DIR/zshrc_src/aliases.zshrc
source $SETUP_DIR/zshrc_src/ps1_updater/gitstatus/gitstatus.prompt.zsh
source $SETUP_DIR/zshrc_src/ps1_updater/update_ps1_preexec
source $SETUP_DIR/zshrc_src/ps1_updater/bash-preexec.sh
source $SETUP_DIR/zshrc_src/pyenv-conda.zshrc
source $SETUP_DIR/zshrc_src/fzf.zshrc
