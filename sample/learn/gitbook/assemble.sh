#!/usr/bin/env bash

sh_current_path=`dirname $0`
echo "current path is $sh_current_path"
folder_name=$sh_current_path/$1
output_file="SUMMARY.md"

if [[ ! -d $folder_name ]]; then
  echo "请输入有效的编译目录: (blog/client/sever)"
  exit -1
fi

cd $folder_name
current_path=`pwd`

echo "current path is $current_path"
echo "# 目录" > $output_file
echo "* [说明](README.md)" >> $output_file

for dir_file in $current_path/*; 
do
  dir_file=`basename $dir_file`
	# echo $dir_file
  if [[ -d $dir_file && $dir_file != "_book" ]]; then
  	echo "valid dir is "$dir_file
  	if [[ -d $dir_file ]]; then
  		md_files=`ls $dir_file`
  		big_title=`basename $dir_file`
  		unset big_title_file
      # echo "  folder markdown file is -> $md_files"
  		for md_file in $md_files; do
        echo "    markdown file is -> $md_file"
        md_file_ex=${md_file##*.}
        echo "    markdown file extend name  -> $md_file_ex"
        if [[ $md_file_ex == "md" ]]; then
          if [[ ! $big_title_file ]]; then
            big_title_file="$dir_file/$md_file"
            out_content="* [ "${big_title}" ](${big_title_file}) "
            echo "    create markdown tilte $out_content"
            echo  "* [ "${big_title}" ](${big_title_file}) " >> $output_file
          fi
          title=`basename $md_file`
          title="${title%.*}"
          out_content="   * [ $title ]($dir_file/$md_file) "
          echo "    add markdown catalogue -> $out_content"
          echo  "   * [ $title ]($dir_file/$md_file)" >> $output_file
        # else
          # echo "$md_file_ex not md"
        fi
  		done
  	fi
  fi
done

# echo `cat README.md` > $output_file