t_file=~/Downloads/auto_log/log_auto_`date +%Y_%m_%d____%H_%M_%S`.txt
echo $t_file
touch echo $t_file
# sh adblogcat.sh $t_file
adb logcat -v threadtime > $t_file
vim $t_file
