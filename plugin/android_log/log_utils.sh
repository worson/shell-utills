alias alog="adb logcat -v threadtime "
alias alogfile="adb logcat -v threadtime > ~/Downloads/auto_log/log_auto_`date "+%Y_%m_%d_%H___%M_%S"`.txt"
alias alogr="adb logcat -v threadtime| grep --color -E "
alias log="adb logcat -v threadtime| grep -E --color $*"
alias logp='_logp(){ echo 111}; _logp() $1'
