
PLUGIN_PATH="$CFG_ROOT_PATH/plugin"

source "$PLUGIN_PATH/adb/adb-sh.sh"

source "$PLUGIN_PATH/docker/docker-shot.sh"

# Android
source $PLUGIN_PATH/android/android-shot.sh

G_CUSTOM_PATH="$PLUGIN_PATH/android"

PATH=$PATH:$G_CUSTOM_PATH
