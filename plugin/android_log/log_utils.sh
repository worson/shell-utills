CFG_ALOG_PATH=$CFG_PLUGIN_PATH"/android_log"
export CFG_ALOG_PATH

#shell tools
alias alogfile="sh $CFG_ALOG_PATH/alogfile.sh"
alias lgglogfile="sh $CFG_ALOG_PATH/langogoLogFile.sh"
alias xalogfile="sh $CFG_ALOG_PATH/xalogfile.sh"
alias alogview="sh $CFG_ALOG_PATH/alogview.sh"

# alias
alias alog="adb logcat -v threadtime "
alias xalog="adb logcat -b main -b system -b radio -v time  "
alias alogls="ls ~/Downloads/auto_log/"
alias alogr="adb logcat -v threadtime| grep --color -E "
alias log="adb logcat -v threadtime| grep -E --color $*"
alias xlog="adb logcat -b main -b system -b radio -v time　| grep -E --color $*"
alias logp='_logp(){ echo 111}; _logp() $1'
