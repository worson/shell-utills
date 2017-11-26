#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json


IS_DEBUG=True

def execute(para):
    print "execute:%s" %(para)
    return os.system(para)

# print "lyrastart  "+argv
if len(sys.argv) >= 1:
    paras={}
    action=None
    val=None
    val2=None
    val3=None
    argv=[]
    for i in range(0,len(sys.argv)):
        v=sys.argv[i]
        if v!='-G':
            argv.append(v)
    if IS_DEBUG:
        print argv
    if(len(argv)>1):
        action=argv[1]
    if(len(argv)>2):
        val=argv[2]
    if(len(argv)>3):
        val2=argv[3]
    if(len(argv)>4):
        val3=argv[4]

    if IS_DEBUG:
        print "input para: action=%s,val=%s,val2=%s,val3=%s" %(action,val,val2,val3)
    configpath='../../config/lyra.json'
    cfgstr=open(configpath).read()
    cfg=json.loads(cfgstr)
    rootpath=cfg['root_path']
    innerapps=['aios','launcher','wechat','music','dialog']
    if action=='info':
        print "get info type: %s" %(val)
        print cfg
        print cfg[val]
        if val=='pkg':
            print 
    
    if action=='cd':
        if val==None: 
            execute("cd %s" %(rootpath))
        elif  val=='build': 
            execute("cd %s | grep 'lyra'" %(rootpath))
    if action=='ls':
        if val==None: 
            execute("ls %s" %(rootpath))
        elif  val=='build': 
            execute("ls %s | grep 'lyra'" %(rootpath))
    if action=='ps':
        if val==None: 
            execute("adb shell ps | grep 'aispeech'")
    if action=='start':
        if val==None:
            execute("adb shell am force-stop ")
        else:
            execute("adb shell am start -n %s" %(cfg[val]['mainactivity']))
        print "start app: %s" %(val)
    if action=='stop':
        print "stop app: %s" %(val)
        if val==None:
            execute("adb shell am force-stop ")
        else:
            execute("adb shell am force-stop %s" %(cfg[val]['pkg']))
    if action=='kill':
        print "stop app: %s" %(val)
        if val==None:
            execute("adb shell am force-stop ")
        else:
            execute("adb shell am force-stop %s" %(cfg[val]['pkg']))
    
    if action=='restart':
        print "restart app: %s" %(val)
    if action=='install':
        print "install app: %s" %(val)
        execute("gradle -p %s installDebug" %('/Users/wangshengxing/project/geek/WaterMonitor/app'))
#

# execute("adb shell ps")


# print os.system("adb shell top")
