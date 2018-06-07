LRAY_ROOT_PATH="/home/sen/project/aispeech/lyra/"
export G_LRAY_ROOT_PATH=$LRAY_ROOT_PATH
export G_LRAY_BLOCK_PATH=$LRAY_ROOT_PATH"/blocks"
export G_LRAY_BUILD_PATH=$LRAY_ROOT_PATH"/tools/build/"

TMP_ANDROID_TOOLS="/home/wangshengxing/Android/Sdk/platform-tools"


PATH=$PATH:$TMP_ANDROID_TOOLS

T_UBUNTU_PATH=$CFG_ROOT_PATH'/ubuntu/'

source  $T_UBUNTU_PATH'app/app-list.sh'

source $T_UBUNTU_PATH'alias/ubuntu_alias.sh'

echo 'ok'
