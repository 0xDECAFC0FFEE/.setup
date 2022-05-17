source /apollo/env/envImprovement/var/zshrc

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
