LRAY_ROOT_PATH="/home/sen/project/aispeech/lyra/"
export G_LRAY_ROOT_PATH=$LRAY_ROOT_PATH
export G_LRAY_BLOCK_PATH=$LRAY_ROOT_PATH"/blocks"
export G_LRAY_BUILD_PATH=$LRAY_ROOT_PATH"/tools/build/"

VIM_PATH="/Applications/MacVim.app/Contents/bin"

PATH=$PATH:$VIM_PATH

export EDITOR=vim

T_MAC_PATH=$CFG_ROOT_PATH'/mac/'

source $T_MAC_PATH'alias/mac-alias.sh'
source $T_MAC_PATH'app/app-list.sh'
source $T_MAC_PATH'app/wine-app.sh'
