#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json
import time


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

def dui_exe(fuc_argv):
    if len(fuc_argv) >= 1:
        paras={}
        action=None
        val0=None
        val=None
        val2=None
        val3=None
        argv=[]
        for i in range(0,len(fuc_argv)):
            v=fuc_argv[i]
            if v!='-G' and v!='-i':
                argv.append(v)
        if IS_DEBUG:
            print argv
        val0=argv[0]
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
        configpath=shpath+'/'+"../../config/%s/dui_prj.json"%(osname)
        cfgstr=open(configpath).read()
        cfg=json.loads(cfgstr)
        rootpath=cfg['root_path']
        innerapps=cfg['apps']
        if action=='location':
            if val==None:
                for appname in innerapps:
                    execute("adb shell pm -p %s" %(cfg[appname]['pkg']))
            elif  val=='build':
                execute("cd %s | grep 'lyra'" %(rootpath))
        elif action=='loglevel':
            if  val !=None:
                print "log level :"+val
                dui_exe([val0,"topic","keys.aios.log.level",val])
        elif action=='keys':
            if val=="set":
                execute("adb shell am broadcast -a action.dui.test.bus.keys.set --es topic %s --es val1 %s " %(val2,val3))
            elif val=="get":
                execute("adb shell am broadcast -a action.dui.test.bus.keys.get --es topic %s" %(val2))
        elif action=='speech':
            if  val !=None:
                execute("adb shell am broadcast -a action.dui.test.speech.state.input --es topic %s" %(val))
        elif action=='topic':
            if  val !=None:
                execute("adb shell am broadcast -a action.dui.test.publish.sdk.msg --es topic %s --es val1 %s " %(val,val2))
        elif action=='xinput':
            if  val !=None:
                dui_exe([val0,"speech","click"])
                time.sleep(1)
                dui_exe([val0,"input",val])
        elif action=='input':
            if  val !=None:
                execute("adb shell am broadcast -a action.dui.test.speech.text.input --es topic %s " %(val))
        elif action=='call':
            if  val !=None:
                if val2 !=None:
                    execute("adb shell am broadcast -a action.dui.test.sdk.node.call --es call %s --es val1 %s " %(val,val2))
                else :
                    execute("adb shell am broadcast -a action.dui.test.sdk.node.call --es call %s " %(val))
        elif action=='sdk':
            if val==None:
                execute("cd %s" %(rootpath))
            elif  val in ['open','close',"return"]:
                execute("adb shell am broadcast -a action.dui.test.publish.sdk.msg --es topic sdk.car.equipment.%s --es val1 %s " %(val,val2))
        elif action=='ls':
            if val==None:
                execute("ls %s" %(rootpath))
            elif  val=='build':
                execute("ls %s | grep 'lyra'" %(rootpath))
            elif val in  innerapps:
                execute("ls %s" %(modulePath(rootpath,val)))
        elif action=='pwd':
            if val in innerapps:
                execute("adb shell pm -p %s" %(cfg[val]['pkg']))
        elif action=='rm':
            if val==None:
                execute("ls %s" %(rootpath))
            elif val in innerapps:
                execute("rm -rf %s/build" %(modulePath(rootpath,val)))
        elif action=='stop':
            if val==None:
                for appname in innerapps:
                    execute("adb shell am force-stop %s" %(cfg[appname]['pkg']))
            elif val in innerapps:
                execute("adb shell am force-stop %s" %(cfg[val]['pkg']))
        elif action=='start':
            if val==None:
                for appname in innerapps:
                    execute("adb shell am start -n %s" %(cfg[appname]['mainactivity']))
            elif val in innerapps:
                execute("adb shell am start -n %s" %(cfg[val]['mainactivity']))
        elif action=='restart':
            dui_exe([val0,"stop",val])
            time.sleep(2)
            dui_exe([val0,"start",val])
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
        elif action=='uninstall':
            if val==None:
                for appname in innerapps:
                    execute("adb uninstall %s" %(cfg[appname]['pkg']))
            elif val in innerapps:
                execute("adb uninstall %s" %(cfg[val]['pkg']))
        elif action=='clear':
            if val==None:
                for appname in innerapps:
                    execute("adb shell pm clear %s" %(cfg[appname]['pkg']))
            elif val in innerapps:
                execute("adb shell pm clear %s" %(cfg[val]['pkg']))
        elif action=='ps':
            if val==None:
                execute("adb shell ps | grep 'dui'")
        elif action=='sign':
            if val==None:
                print cmd("uname")
            else :
                sh=cfg["signs"][val]['sh']
                dst=os.path.splitext(val2)
                signsh="%s %s %s"%(sh,val2,dst[0]+"-signed"+dst[1])
                execute(signsh)
                #print signsh
        elif action=='build':
            if val==None:
                print 'build all'
                cmds=[]
                buldsh=rootpath+"/"+cfg["build_tool"]
                cmds.append("cd %s" %(os.path.dirname(buldsh)))
                cmds.append("sh %s" %(buldsh))
                executes(cmds)
        elif action=='assemble':
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



dui_exe(sys.argv)
# execute("adb shell ps")


# print os.system("adb shell top")
