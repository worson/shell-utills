t_device_path="/sdcard/demo.mp4"
t_file_name=~/Downloads/auto_record/record_`date "+%Y_%m_%d_%H___%M_%S"`.mp4 ;
adb pull  $t_device_path $t_file_name
open $t_file_name ;
