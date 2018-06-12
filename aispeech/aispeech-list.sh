
AISPEECH_PATH="$CFG_ROOT_PATH/aispeech"
export AISPEECH_PATH

# lyra
source  $AISPEECH_PATH'/alias/lyra.sh'
# lyra cmd
source $AISPEECH_PATH"/project/lyra_cmd/lyra_cmd_list.sh"

# project
source $AISPEECH_PATH/project/project-list.sh

G_CUSTOM_PATH="$AISPEECH_PATH/project/":"$AISPEECH_PATH/project/dui":"$AISPEECH_PATH/project/lyra"
PATH=$PATH:$G_CUSTOM_PATH

#echo aispeech
