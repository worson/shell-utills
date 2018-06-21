t_file_name=~/Downloads/android_screen/picture_`date "+%Y_%m_%d_%H___%M_%S"`.png ;
echo "start , $t_file_name"
adb exec-out screencap -p > $t_file_name ;
# open $t_file_name ;
