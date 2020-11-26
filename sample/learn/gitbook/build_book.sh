#!/usr/bin/env bash

sh_current_path=`dirname $0`

for dir_file in $sh_current_path/*;
do
    if [[ -d $dir_file ]]; then
        echo "********** start build gitbook  -> $dir_file ***********************************"
        sh ./assemble.sh $dir_file
        gitbook build ./$dir_file
        echo "********** end build gitbook  -> $dir_file ***********************************"
    fi
done 