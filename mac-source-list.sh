#!/bin/bash
sourcepath="/Users/wangshengxing/project/mygithub/shell-utills"
CFG_ROOT_PATH=$sourcepath

SH=zsh
export SH

#source  $sourcepath/wine-app.sh
# common
source  $sourcepath/source-list.sh
source  $sourcepath/mac/ev.sh

export CFG_ROOT_PATH


[ -f /usr/local/etc/profile.d/autojump.sh ] && . /usr/local/etc/profile.d/autojump.sh