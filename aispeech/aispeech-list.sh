
AISPEECH_PATH="$CFG_ROOT_PATH/aispeech"
# lyra
source  $AISPEECH_PATH'/alias/lyra.sh'
# project
source $AISPEECH_PATH/project/project-list.sh

G_CUSTOM_PATH="$AISPEECH_PATH/project/":"$AISPEECH_PATH/project/dui":"$AISPEECH_PATH/project/lyra"
PATH=$PATH:$G_CUSTOM_PATH
