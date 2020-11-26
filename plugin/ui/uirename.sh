#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import json
import csv
import shutil
import commands


def filterParas(paras):
  if len(paras) >= 1:
    action = None
    val = None
    val2 = None
    val3 = None
    argv = []
    for i in range(0, len(paras)):
      v = sys.argv[i]
      if v != '-G' and v != '-i':
        argv.append(v)
    if (len(argv) > 1):
      action = argv[1]
    if (len(argv) > 2):
      val = argv[2]
    if (len(argv) > 3):
      val2 = argv[3]
    if (len(argv) > 4):
      val3 = argv[4]
  return argv


def handle(paras):
  if len(paras) >= 1:
    action = None
    val1 = None
    val2 = None
    val3 = None
    argv = filterParas(paras)
    if (len(argv) > 1):
      action = argv[1]
    if (len(argv) > 2):
      val1 = argv[2]
    if (len(argv) > 3):
      val2 = argv[3]
    if (len(argv) > 4):
      val3 = argv[4]
    print ("input para: action=%s,val1=%s,val2=%s,val3=%s" % (action, val1, val2, val3))
    if (action=="rename"):
        (status, output) = commands.getstatusoutput('pwd')
        # print(commands.getstatusoutput('pwd'))
        renameDirIcon(output,val1,val2)



def renameDirIcon(dir,s_name,d_name):
    print("renameDirIcon para: source=%s,destination=%s" % (s_name, d_name))
    

if __name__ == '__main__':
  handle(sys.argv)
