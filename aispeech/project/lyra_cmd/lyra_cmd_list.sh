LYRA_PROJECT_PATH=$AISPEECH_PATH"/project/lyra_cmd"

alias lyrainstall="$CFG_BASH $LYRA_PROJECT_PATH/lyrainstall.sh"
alias lyrauninstall="$CFG_BASH $LYRA_PROJECT_PATH/lyrauninstall.sh"
alias lyrastart="$CFG_BASH $LYRA_PROJECT_PATH/lyrastart.sh"
alias lyrastop="$CFG_BASH $LYRA_PROJECT_PATH/lyrastop.sh"
alias lyrapush="$CFG_BASH $LYRA_PROJECT_PATH/lyrapush.sh"


#git
alias lyragit='t_lyragit(){repolyra cmd "git $*" ; }; t_lyragit'
alias lyrapull="repolyra cmd "git pull $1 $2 $3 $4""
alias lyrapush="repolyra cmd "git push $1 $2 $3 $4""

#lyra
alias fswx='_gfile(){ grep -E "doEngine: message -> " $* }; _gfile $*'
