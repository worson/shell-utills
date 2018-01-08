#!/bin/bash
adb root
adb remount

echo ">>>uninstall lyra-daemon..."
adb uninstall com.aispeech.aios
adb shell rm -rf /system/app/lyra-daemon

echo ">>>uninstall lyra-dialog..."
adb uninstall com.aispeech.lyra.dialog
adb shell rm -rf /system/app/lyra-dialog

echo ">>>uninstall lyra-launcher..."
adb uninstall com.aispeech.launcher
adb shell rm -rf /system/app/lyra-launcher

echo ">>>uninstall lyra-music..."
adb uninstall com.aispeech.aios.adapter
adb shell rm -rf /system/app/lyra-music

echo ">>>uninstall lyra-wechat..."
adb uninstall com.aispeech.wechat.presenter
adb shell rm -rf /system/app/lyra-wechat

adb shell rm -rf /data/data/com.aispeech.*
adb shell rm -rf /data/app/com.aispeech.*

