
CFG_PLUGIN_PATH="$CFG_ROOT_PATH/plugin"
export CFG_PLUGIN_PATH

source "$CFG_PLUGIN_PATH/adb/adb-sh.sh"

source "$CFG_PLUGIN_PATH/docker/docker-shot.sh"

# Android cmd
source $CFG_PLUGIN_PATH/android_cmd/android-shot.sh


#
source $CFG_PLUGIN_PATH/android_log/log_utils.sh




G_CUSTOM_PATH="$CFG_PLUGIN_PATH/android_cmd"
G_CUSTOM_PATH=$G_CUSTOM_PATH:"$PLUGIN_PATH/ssh_cmd"

PATH=$PATH:$G_CUSTOM_PATH
