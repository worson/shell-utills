#!/usr/bin/env bash

sh_current_path=`dirname $0`
current_path=`pwd`

for dir_file in $current_path/*; 
do
    if [[ -d $dir_file ]]; then
        echo $dir_file
        base_dir_file=`basename $dir_file`
        zip -r $base_dir_file".zip"   $base_dir_file
    fi
done