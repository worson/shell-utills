LRAY_ROOT_PATH="/home/sen/project/aispeech/lyra/"
export G_LRAY_ROOT_PATH=$LRAY_ROOT_PATH
export G_LRAY_BLOCK_PATH=$LRAY_ROOT_PATH"/blocks"
export G_LRAY_BUILD_PATH=$LRAY_ROOT_PATH"/tools/build/"

VIM_PATH="/Applications/MacVim.app/Contents/bin"
PROTOC_PATH="/Users/wangshengxing/project/tools/protoc-3.6.0-osx-x86_64/bin"
MYSQL_PATH="/usr/local/mysql/bin"

FLUTTER_PATH="/Users/Shared/AppShared/flutter/bin"
export PUB_HOSTED_URL=https://pub.flutter-io.cn #国内用户需要设置
export FLUTTER_STORAGE_BASE_URL=https://storage.flutter-io.cn #国内用户需要设置

ANDROID_HOME="/Users/Shared/ShareLib/Android/sdk/"
ANDROID_TOOL_PATH="/Users/Shared/ShareLib/Android/sdk/platform-tools"


PATH=$PATH:$VIM_PATH:$PROTOC_PATH:$ANDROID_TOOL_PATH:$FLUTTER_PATH:$MYSQL_PATH

export EDITOR=vim

T_MAC_PATH=$CFG_ROOT_PATH'/mac/'

source $T_MAC_PATH'alias/mac-alias.sh'
source $T_MAC_PATH'alias/ssh-alias.sh'
source $T_MAC_PATH'app/app-list.sh'
source $T_MAC_PATH'app/wine-app.sh'
