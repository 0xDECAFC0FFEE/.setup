export PATH=$HOME/.toolbox/bin:$PATH
export PATH=$HOME/jdk-11.0.13+8/bin:$PATH

alias bb='brazil-build'
alias sam="brazil-build-tool-exec sam"

export SAM_REGION=us-west-2
export SAM_CONDUIT_ADMIN_ACCOUNT_ID="219339085096"
export SAM_ASSUME_ACCOUNT_ID="219339085096"    

export CONDUIT_ADMIN_ACCOUNT_ID=219339085096
export CONDUIT_ADMIN_ACCOUNT_ROLE="IibsAdminAccess-DO-NOT-DELETE"
export PERSONAL_ACCOUNT_ID=$CONDUIT_ADMIN_ACCOUNT_ID

function kcurl() {
  curl -k --location-trusted --negotiate -u: -c /tmp/cookies.txt -b /tmp/cookies.txt "$@"
}

alias bbb='brazil-recursive-cmd --allPackages brazil-build'
alias bre='brazil-runtime-exec'
alias bbb-clean='brazil-recursive-cmd --allPackages brazil-build --reverse clean'

# export TOD_CUSTOMER_CREDENTIAL_PATH=/home/tongluca/.aws/credentials

function git-reattach-head() {
    if [ "$#" -eq 1 ]; then
        if [[ "$1" == "--help" ]]; then
            echo "usage: [--branch BRANCH]\n"
            echo "completely nukes git history and reattaches head from whatever branch you input without touching the package directory\n"
            echo "optional arguments: \n   --branch BRANCH git branch to pull from [default: mainline]"
            return
        else
            echo "unrecognized argument $1"
        fi
    fi

    if [ "$#" -eq 2 ]; then
        if [[ "$1" == "--branch" ]]; then
            GIT_BRANCH="$2"
        else
            echo "unrecognized arguments $1 $2"
        fi
    else
        GIT_BRANCH="mainline"
    fi

    WORKSPACE_ROOT=`brazil-path workspace-root 2> /dev/null` && \
    PACKAGE_NAME=`brazil-path package-name 2> /dev/null` && \

    TEMP_PACKAGE_PATH="$HOME/temp/temp_package_path/"$PACKAGE_NAME && \
    PACKAGE_PATH=$WORKSPACE_ROOT"/src/"$PACKAGE_NAME && \

    echo "reattaching git head at branch "$GIT_BRANCH" for package "$PACKAGE_NAME" in workspace "$WORKSPACE_ROOT && \
    
    CURRENT_PATH=`pwd` && \
    cd $WORKSPACE_ROOT && \
    mkdir -p "$HOME/temp/temp_package_path" 2> /dev/null && \
    rm -rf $TEMP_PACKAGE_PATH 2> /dev/null && \
    
    echo "moving $PACKAGE_PATH to $TEMP_PACKAGE_PATH"
    mv $PACKAGE_PATH $TEMP_PACKAGE_PATH && \
    
    echo "pulling $PACKAGE_NAME from gitfarm"
    brazil ws use -p $PACKAGE_NAME && \
    cd $PACKAGE_PATH && \
    git fetch --all && \
    git checkout $GIT_BRANCH && \
    
    echo "moving $PACKAGE_PATH/.git to $TEMP_PACKAGE_PATH/.git"
    rm -rf $TEMP_PACKAGE_PATH/.git 2> /dev/null && \
    mv $PACKAGE_PATH/.git $TEMP_PACKAGE_PATH/.git && \
    cd $WORKSPACE_ROOT && \
    
    echo "moving $TEMP_PACKAGE_PATH back to $PACKAGE_PATH"
    rm -rf $PACKAGE_PATH && \
    mv $TEMP_PACKAGE_PATH $PACKAGE_PATH && \
    cd $CURRENT_PATH
}
