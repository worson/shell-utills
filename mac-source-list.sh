#!/bin/bash
sourcepath="/Users/wangshengxing/tool/shell-config"
CFG_ROOT_PATH=$sourcepath


#source  $sourcepath/wine-app.sh
# common
source  $sourcepath/source-list.sh

source  $sourcepath/ubuntu/app-list.sh
source  $sourcepath/ubuntu/ev.sh

export CFG_ROOT_PATH
