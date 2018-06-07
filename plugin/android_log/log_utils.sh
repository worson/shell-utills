alias alog="adb logcat -v threadtime "
alias alogfile=" t_file=~/Downloads/auto_log/log_auto_`date +%Y_%m_%d____%H_%M_%S`.txt && echo $t_file && touch echo $t_file && adb logcat -v threadtime > $t_file "
alias alogview=" t_file=~/Downloads/auto_log/log_auto_`date +%Y_%m_%d____%H_%M_%S`.txt && echo $t_file && touch echo $t_file && adb logcat -v threadtime > $t_file && vim $t_file"
alias alogls="ls ~/Downloads/auto_log/"
alias alogr="adb logcat -v threadtime| grep --color -E "
alias log="adb logcat -v threadtime| grep -E --color $*"
alias logp='_logp(){ echo 111}; _logp() $1'
