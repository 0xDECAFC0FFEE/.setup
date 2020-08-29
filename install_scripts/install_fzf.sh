#! /bin/bash
# installs fzf

if ! [ -d ~/.fzf ]
then
    echo "downloading fzf"
    git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
else
    echo "skipping fzf download"
fi

if ! command -v fzf &> /dev/null
then
	echo "installing fzf"
	~/.fzf/install --key-bindings --completion --update-rc
else
    echo "fzf already detected - skipping install"
fi

