CFG_ALOG_PATH=$CFG_PLUGIN_PATH"/android_log"
export CFG_ALOG_PATH

#shell tools
alias alogfile="sh $CFG_ALOG_PATH/alogfile.sh"
alias alogview="sh $CFG_ALOG_PATH/alogview.sh"

# alias
alias alog="adb logcat -v threadtime "
alias alogls="ls ~/Downloads/auto_log/"
alias alogr="adb logcat -v threadtime| grep --color -E "
alias log="adb logcat -v threadtime| grep -E --color $*"
alias logp='_logp(){ echo 111}; _logp() $1'
