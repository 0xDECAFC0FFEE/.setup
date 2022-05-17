# source /apollo/env/envImprovement/var/zshrc
export SETUP_DIR=$HOME/.setup
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
    source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

export DISABLE_AUTO_UPDATE=true
ZSH_THEME="powerlevel10k/powerlevel10k"
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

plugins=(git fzf-docker ripgrep fzf-tab zsh-autosuggestions)
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
    
    export LDFLAGS="-L/usr/local/opt/zlib/lib"
    export CPPFLAGS="-I/usr/local/opt/zlib/include"
    export PKG_CONFIG_PATH="/usr/local/opt/zlib/lib/pkgconfig"
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
_comp_options+=(globdots)

dotfile_dir=$SETUP_DIR/zshrc_src/rc_dotfiles
source $dotfile_dir/aliases.zshrc
source $dotfile_dir/ps1_updater/update_ps1_preexec
source $dotfile_dir/ps1_updater/bash-preexec.sh
source $dotfile_dir/fzf.zshrc
source $dotfile_dir/pyenv-conda.zshrc
# source $dotfile_dir/amazon_aliases.zshrc

chpwd() ls
