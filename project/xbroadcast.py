#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json
import xadb
import parastool
import putils
import xadb



def handle(paras):
    if len(paras) >= 1:
        action=None
        val=None
        val2=None
        val3=None
        argv=parastool.filterParas(paras)
        if(len(argv)>1):
            action=argv[1]
        if(len(argv)>2):
            val=argv[2]
        if(len(argv)>3):
            val2=argv[3]
        if(len(argv)>4):
            val3=argv[4]

        print "input para: action=%s,val=%s,val2=%s,val3=%s" %(action,val,val2,val3)
        shpath=os.path.dirname(argv[0])
        macos=("Darwin" in putils.cmd('uname')[0])
        #print "macos " macos
        osname=('mac' if macos else 'ubuntu')
        configpath=shpath+'/'+"../config/%s/lyra_auto.json"%(osname)
        cfgstr=open(configpath).read()
        cfg=json.loads(cfgstr)
        # rootpath=cfg['root_path']
        # innerapps=['aios','launcher','wechat','music','dialog']
        if action=='api':
            duiapi=open(cfg["duiApis"][val]).read()
            content=json.loads(duiapi)
            value={}
            value["pkgName"]=content["pkg"]
            value["provider"]=content["provider"]
            value["action"]=content["action"]
            value["command"]=val2
            value["data"]="{}"
            data={}
            data["value"]=value
            fdata=json.dumps(value).replace(' ','').replace('\"','\\\"').replace('}','\}')
            cmd="adb shell am broadcast -a com.ileja.voice.mock.test --es type %s --es value %s" %("dui.command","\""+fdata+"\"")
            print cmd
            putils.cmd(cmd)
        elif if action=='send':
            duiapi=open(cfg["duiApis"][val]).read()
            content=json.loads(duiapi)
            value={}
            value["domain"]=content["domain"]
            value["provider"]=content["provider"]
            value["action"]=content["action"]
            value["type"]=val2
            value["value"]="{}"
            data={}
            data["value"]=value
            fdata=json.dumps(value).replace(' ','').replace('\"','\\\"').replace('}','\}')
            cmd="adb shell am broadcast -a com.ileja.voice.mock.test --es type %s --es value %s" %("router.command","\""+fdata+"\"")
            print cmd
            putils.cmd(cmd)

if __name__ == '__main__':
    handle(sys.argv)
