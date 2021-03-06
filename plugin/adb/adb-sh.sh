
alias acat="adb shell cat "
alias aremount="adb remount"
alias ashot="adb exec-out screencap -p > "
#alias ashotfile="_ashotfile(){t_file_name=~/Downloads/android_screen/picture_`date "+%Y_%m_%d_%H___%M_%S"`.png ; adb exec-out screencap -p > $t_file_name ; open $t_file_name ; }; _ashotfile"
alias adevices="adb device"
alias adate="adb shell date"
alias akill="adb shell kill "
alias apull="adb pull "
alias apush="adb push "
alias areboot="adb reboot "
alias ain="adb install "
alias aun="adb uninstall "
alias als="adb shell ls "
alias arm="adb shell rm "
alias atouch="adb shell touch "
alias amv="adb shell mv "
alias amkdir="adb shell mkdir "
alias as="adb shell "
alias ash="adb shell "
alias aas="adb shell am start -n "
alias abc="adb shell am broadcast -a "
alias aping="adb shell ping www.baidu.com"
alias abm="adb shell bmgr"
alias abackup="adb shell bmgr backup "

alias atop="adb shell top"
alias aps="adb shell ps"
alias apsr="adb shell ps | grep "
alias astop="adb shell am force-stop"
alias aclear="adb shell pm clear"
alias acl="adb shell pm clear"
alias apl="adb shell pm -l"
alias aplr="adb shell pm -l | grep "
alias app="adb shell pm -p"


#设备信息相关
alias aserial="adb get-serialno"
alias asn="adb get-serialno"
alias awindow="adb shell dumpsys window w | grep \/  |  grep name="


#事件输入相关
alias aback="adb shell input keyevent 4"
alias ahome="adb shell input keyevent 3"
alias akey="adb shell input keyevent "
alias atxt="adb shell input text "

# 显示应用信息
alias apkinfo="aapt dump badging "

#app
alias appsetting="adb shell am start com.android.settings/com.android.settings.Settings"

# aispeech
alias swake="adb shell am broadcast -a aios.intent.action.UI_MIC_CLICK"
alias ssetting="adb shell am start com.aispeech.aios/.SettingActivity"
alias sbridge="adb shell am start com.aispeech.aios.bridge/.activity.MainActivity"

# aispeech log
#alias lasa="adb logcat -v threadtime | grep lasa"
#alias aios="adb logcat -v threadtime | grep aios"


# tool
alias np="wine /Users/wangshengxing/tool/wine/npp.7.3.3.bin/notepad++.exe "

# 屏幕相关
alias afrontactivity2="adb shell dumpsys activity top | grep ACTIVITY"
