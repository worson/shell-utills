#!/usr/bin/env python
# coding=utf-8
import sys
import os
import platform
import json
import fileUtil as fu
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
    innerapps=['aios','launcher','wechat','music','dialog']
    if action=='pull':
        if val==None: 
            print "pull data ,current path:%s"%(os.path.curdir)
        elif  val=='build': 
            execute("cd %s | grep 'lyra'" %(rootpath))
    elif action=='analyse':
        if val==None:
            print "start analyse ..."
            files=fu.getFolderFiles('.','\S+\.json',recursive=True)
            print "files\n",files 
            events={}
            f=files[0]
            gpsevents=[]
            for f in files:
                upstr=open(f).read()
                upjson=json.loads(upstr)
                msgs=upjson['messages']
                #print len(msgs),type(msgs)
                tekeys=msgs.keys()
                for tekey in tekeys :
                    tevents=msgs[tekey]
                    if tekey in events.keys():
                        events[tekey]=len(tevents)+events[tekey]
                    else :
                        events[tekey]=len(tevents)
                    if tekey=='gps_event':
                        for e in tevents:
                            gpsevents.append(e)
    #                        print e['rtc']
                    #print len(tevents)

            print events
            allevent=0
            for e in events.keys():
                allevent=allevent+events[e]
            print 'all event size:',allevent

            with open("./hmm.json",'w') as json_file:
                json.dump(gpsevents,json_file,ensure_ascii=False)
