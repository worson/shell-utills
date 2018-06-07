#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json
import putils
import parastool


IS_DEBUG=True

def modulePath(rootpath,name):
    return "%s/blocks/lyra-%s" %(rootpath,name)
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

        if IS_DEBUG:
            print "input para: action=%s,val=%s,val2=%s,val3=%s" %(action,val,val2,val3)
        shpath=os.path.dirname(argv[0])
        macos=("Darwin" in putils.cmd('uname')[0])
        #print "macos " macos
        osname=('mac' if macos else 'ubuntu')
        # configpath=shpath+'/'+"../../config/%s/lyra.json"%(osname)
        # cfgstr=open(configpath).read()
        # cfg=json.loads(cfgstr)
        # rootpath=cfg['root_path']
        # innerapps=['aios','launcher','wechat','music','dialog']
        if action=='broadcast':
            intent=val
            dir=(putils.cmd('pwd')[0])+"/"+val2
            dir=dir.replace('\n','')
            print dir
            data=open(dir).read().replace(' ','').replace('\"','\\\"').replace('}','\}')
            data="\'"+data+"\'"
            data=data.replace('\n','')
            print data
            cmd="adb shell am broadcast -a %s %s" %(intent,data)
            # cmd="adb shell am broadcast -a action.test.dui.status.set --es key navi --es value %s" %(data)

            # print cmd
            putils.execute(cmd)
if __name__ == '__main__':
    handle(sys.argv)
