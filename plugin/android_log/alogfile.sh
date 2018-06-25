t_file=~/Downloads/auto_log/log_auto_`date +%Y_%m_%d____%H_%M_%S`.txt
if [  -n "$1" ]; then
  t_file=~/Downloads/auto_log/$1_custom_`date +%Y_%m_%d____%H_%M_%S`.txt
fi
echo $t_file
touch  $t_file
# sh adblogcat.sh $t_file
adb logcat -v threadtime > $t_file
vim $t_file
