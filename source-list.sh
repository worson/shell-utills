sourcepath="/Users/wangshengxing/tool/shell-config"
source  $sourcepath/adb-sh.cfg
source  $sourcepath/onekey-sh.sh
source  $sourcepath/sign-apk.sh
source  $sourcepath/wine-app.sh

# Android
source $sourcepath/android/android-shot.sh

# project
source $sourcepath/project/project-list.sh

# PATH
G_CUSTOM_PATH="$sourcepath/android"
G_CUSTOM_PATH=$G_CUSTOM_PATH:"$sourcepath/project/lyra"

CURPATH=`pwd`
SHELL_PATH=$CURPATH"/shell"
# echo "current path is "$CURPATH
# export PATH=$PATH:$SHELL_PATH
# echo "PATH is "$PATH

PATH=$PATH:$G_CUSTOM_PATH
