#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json


IS_DEBUG=True
def cmd(para):
    print "execute:%s" %(para)
    #return os.system(para)
    return os.popen(para).readlines()
def execute(para):
    print "execute:%s" %(para)
    return os.system(para)
    #return os.popen(para).readlines()
def executes(paras):
    print "execute:%s" %(paras)
    cmd=''
    for c in paras:
        cmd=cmd+' \n '+c;
    return os.system(cmd)
    #return os.popen(paras).readlines()
def modulePath(rootpath,name):
    return "%s/blocks/lyra-%s" %(rootpath,name)
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
        if v!='-G' and v!='-i':
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
    shpath=os.path.dirname(argv[0])
    macos=("Darwin" in cmd('uname')[0])
    #print "macos " macos
    osname=('mac' if macos else 'ubuntu')
    configpath=shpath+'/'+"../../config/%s/lyra.json"%(osname)
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
    if action=='test':
        cmds=[]
        cmds.append('ls /')
        cmds.append('ls ~')
        executes(cmds)
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
        elif val in  innerapps:
            execute("ls %s" %(modulePath(rootpath,val)))
    if action=='pwd':
        if val in innerapps:
            execute("adb shell pm -p %s" %(cfg[val]['pkg']))
    if action=='rm':
        if val==None:
            execute("ls %s" %(rootpath))
        elif val in innerapps:
            execute("rm -rf %s/build" %(modulePath(rootpath,val)))
    if action=='stop':
        if val in innerapps:
            execute("adb shell am force-stop %s" %(cfg[val]['pkg']))
    elif action=='install':
        if val==None:
            for appname in innerapps:
                execute("adb push %s  %s" %(rootpath+"/"+cfg[appname]['debugapk'],"/data/local/tmp/"+cfg[appname]['pkg']))
                execute("adb shell pm install -t -r  %s" %("/data/local/tmp/"+cfg[appname]['pkg']))
                time.sleep(2)
        elif val in innerapps:
            appname=val
            srcapp=rootpath+"/"+cfg[appname]['debugapk']
            if val2 !=None :
                srcapp=val2
            execute("adb push %s  %s" %(srcapp,"/data/local/tmp/"+cfg[appname]['pkg']))
            execute("adb shell pm install -t -r  %s" %("/data/local/tmp/"+cfg[appname]['pkg']))
        elif val!=None:
            tname="/data/local/tmp/tmpapk/common.apk"
            execute("adb push %s  %s" %(val,tname))
            execute("adb shell pm install -t -r  %s" %(tname))
    if action=='uninstall':
        if val==None:
            print "uninstall all lyra app ..."
            #execute("sh %s"%(os.path.abspath("./lyrauninstall.sh")))
            execute("sh %s"%(shpath+"/"+"lyrauninstall.sh"))
        elif val in innerapps:
            execute("adb shell am force-stop %s" %(cfg[val]['pkg']))
    if action=='ps':
        if val==None:
            execute("adb shell ps | grep 'aispeech'")
    if action=='sign':
        if val==None:
            print cmd("uname")
        else :
            sh=cfg["signs"][val]['sh']
            dst=os.path.splitext(val2)
            signsh="%s %s %s"%(sh,val2,dst[0]+"-signed"+dst[1])
            execute(signsh)
            #print signsh
    if action=='build':
        if val==None:
            print 'build all'
            cmds=[]
            buldsh=rootpath+"/"+cfg["build_tool"]
            cmds.append("cd %s" %(os.path.dirname(buldsh)))
            cmds.append("sh %s" %(buldsh))
            executes(cmds)
    if action=='assemble':
        if val==None:
            execute("adb shell am force-stop ")
        else:
            cmds=[]
            buildfile="%s/blocks/lyra-%s/build.sh" %(rootpath,val)
            filepath=os.path.dirname(buildfile)
            cmds.append("cd %s" %(filepath))
            cmds.append("pwd")
            cmds.append("sh %s/blocks/lyra-%s/build.sh" %(rootpath,val))
            executes(cmds)


# execute("adb shell ps")


# print os.system("adb shell top")
