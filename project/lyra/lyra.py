#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform


def execute(para):
    return os.system(para)

# print "lyrastart  "+sys.argv
if len(sys.argv) >= 3:
    inputlen=len(sys.argv)
    paras={}
    action=sys.argv[1]
    val=sys.argv[2]
    # print "lyrastart  action=%s,val=%s" %(action,val)
    if action=='start':
        print "start app: %s" %(val)
    if action=='stop':
        print "stop app: %s" %(val)
    if action=='restart':
        print "restart app: %s" %(val)
    if action=='install':
        print "install app: %s" %(val)
        execute("gradle -p %s installDebug" %('/Users/wangshengxing/project/geek/WaterMonitor/app'))
#

# execute("adb shell ps")


# print os.system("adb shell top")
