
CFG_PLUGIN_PATH="$CFG_ROOT_PATH/plugin"
export CFG_PLUGIN_PATH

source "$CFG_PLUGIN_PATH/adb/adb-sh.sh"

source "$CFG_PLUGIN_PATH/docker/docker-shot.sh"

# Android cmd
source $CFG_PLUGIN_PATH/android_cmd/android-shot.sh


#
source $CFG_PLUGIN_PATH/android_log/log_utils.sh
source $CFG_PLUGIN_PATH/shell/shell-source.sh

alias ascreen="sh $CFG_PLUGIN_PATH/android_screen/android_screen.sh"
alias apktool="sh $CFG_PLUGIN_PATH/apk_tool/apktool"
alias dex2jar="sh $CFG_PLUGIN_PATH/dex2jar/d2j-dex2jar.sh"

alias asign="sh $CFG_PLUGIN_PATH/apk_sign/asign.sh"

G_UI_PATH="$CFG_PLUGIN_PATH/ui"


G_CUSTOM_PATH="$CFG_PLUGIN_PATH/android_cmd":"$CFG_PLUGIN_PATH:aosp"
G_CUSTOM_PATH=$G_CUSTOM_PATH:"$PLUGIN_PATH/ssh_cmd":$G_UI_PATH



PATH=$PATH:$G_CUSTOM_PATH


