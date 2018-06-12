LYRA_PROJECT_PATH=$AISPEECH_PATH"/project/lyra_cmd"

alias lyrainstall="sh $LYRA_PROJECT_PATH/lyrainstall.sh"
alias lyrauninstall="sh $LYRA_PROJECT_PATH/lyrauninstall.sh"
alias lyrastart="sh $LYRA_PROJECT_PATH/lyrastart.sh"
alias lyrastop="sh $LYRA_PROJECT_PATH/lyrastop.sh"
alias lyrapush="sh $LYRA_PROJECT_PATH/lyrapush.sh"


#git
alias lyragit="repolyra cmd git $1"
alias lyrapull="repolyra cmd "git pull $1 $2 $3 $4""
alias lyrapush="repolyra cmd "git push $1 $2 $3 $4""
