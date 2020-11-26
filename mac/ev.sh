LRAY_ROOT_PATH="/home/sen/project/aispeech/lyra/"
export G_LRAY_ROOT_PATH=$LRAY_ROOT_PATH
export G_LRAY_BLOCK_PATH=$LRAY_ROOT_PATH"/blocks"
export G_LRAY_BUILD_PATH=$LRAY_ROOT_PATH"/tools/build/"

VIM_PATH="/Applications/MacVim.app/Contents/bin"

FLUTTER_PATH="~/app/flutter/bin"
export PUB_HOSTED_URL=https://pub.flutter-io.cn #国内用户需要设置
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn #国内用户需要设置


PATH=$PATH:$VIM_PATH:$FLUTTER_PATH

export EDITOR=vim

#x export
# export X_GRADLE_PATH=/Users/wangshengxing/tool/gradle/gradle-5.6.4/bin/gradle

T_MAC_PATH=$CFG_ROOT_PATH'/mac/'

source $T_MAC_PATH'alias/mac-alias.sh'
source $T_MAC_PATH'alias/ssh-alias.sh'
source $T_MAC_PATH'app/app-list.sh'
source $T_MAC_PATH'app/wine-app.sh'
