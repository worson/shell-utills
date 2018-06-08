
PLUGIN_PATH="$CFG_ROOT_PATH/plugin"

source "$PLUGIN_PATH/adb/adb-sh.sh"

source "$PLUGIN_PATH/docker/docker-shot.sh"

# Android
source $PLUGIN_PATH/android_cmd/android-shot.sh

#
source $PLUGIN_PATH/android_log/log_utils.sh


G_CUSTOM_PATH="$PLUGIN_PATH/android_cmd"
G_CUSTOM_PATH=$G_CUSTOM_PATH:"$PLUGIN_PATH/ssh_cmd"

PATH=$PATH:$G_CUSTOM_PATH
