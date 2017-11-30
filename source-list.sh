
source  $sourcepath/adb-sh.cfg
source $sourcepath/adb-sh.cfg
source  $sourcepath/onekey-sh.sh
source  $sourcepath/sign-apk.sh



# lyra
source  $sourcepath/lyra/lyra.sh

# Android
source $sourcepath/android/android-shot.sh

# project
source $sourcepath/project/project-list.sh

# system
source $sourcepath/system/system-list.sh

# PATH
SYSTEM_TOOL_PATH=$sourcepath/system
VIM_PATH="/Applications/MacVim.app/Contents/bin"
G_CUSTOM_PATH="$sourcepath/android" 
G_CUSTOM_PATH=$G_CUSTOM_PATH:"$sourcepath/project/lyra":$VIM_PATH:$SYSTEM_TOOL_PATH

CURPATH=$sourcepath
SHELL_PATH=$CURPATH"/shell" 
# echo "current path is "$CURPATH
# export PATH=$PATH:$SHELL_PATH
# echo "PATH is "$PATH

PATH=$PATH:$SHELL_PATH:$G_CUSTOM_PATH
