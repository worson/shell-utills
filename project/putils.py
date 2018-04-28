#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json

# 执行系统相关的指令和系统相关的工具类

IS_DEBUG=True
# 执行系统指令，并返回结果
def cmd(para):
    print "execute:%s" %(para)
    #return os.system(para)
    return os.popen(para).readlines()
# 执行系统指令
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

def handle(paras):
    if len(paras) >= 1:
        paras={}
        action=None
        val=None
        val2=None
        val3=None
        argv=[]
        for i in range(0,len(paras)):
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

if __name__ == '__main__':
    handle(sys.argv)
