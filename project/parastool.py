#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import platform
import json
# 参数相关的处理工具

def filterParas(paras):
    if len(paras) >= 1:
        action=None
        val=None
        val2=None
        val3=None
        argv=[]
        for i in range(0,len(paras)):
            v=sys.argv[i]
            if v!='-G' and v!='-i':
                argv.append(v)
        if(len(argv)>1):
            action=argv[1]
        if(len(argv)>2):
            val=argv[2]
        if(len(argv)>3):
            val2=argv[3]
        if(len(argv)>4):
            val3=argv[4]
    return argv

if __name__ == '__main__':
    print sys.argv
    print filterParas(sys.argv)
