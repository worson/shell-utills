#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Just for clone and pull code

from xml.dom.minidom import parse
import xml.dom.minidom
import os
import shutil
import sys
import platform
import json

IS_DEBUG = True


def cmd(para):
    print "execute:%s" % (para)
    # return os.system(para)
    return os.popen(para).readlines()


def execute(para):
    print "execute:%s" % (para)
    return os.system(para)
    # return os.popen(para).readlines()


def executes(paras):
    print "execute:%s" % (paras)
    cmd = ''
    for c in paras:
        cmd = cmd + ' \n ' + c;
    return os.system(cmd)


# parse manifest.xml
class xmlUtil:
    def __init__(self, xmlName):
        self.xmlName = xmlName
        if not os.path.isfile(self.xmlName):
            print 'Manifest.xml is not exists, please check it'
            os._exit(-1)
        self.domTree = xml.dom.minidom.parse(self.xmlName)
        self.collection = self.domTree.documentElement

    def parseXml(self):
        print 'Start parse manifest.xml'
        appInfos = []

        # get applications info
        self.applications = self.collection.getElementsByTagName("application")
        for application in self.applications:
            appInfo = {}
            if application.hasAttribute("addr"):
                # print application.getAttribute("addr")
                appInfo["addr"] = application.getAttribute("addr")
            if application.hasAttribute("path"):
                # print application.getAttribute("path")
                appInfo["path"] = application.getAttribute("path")
            if application.hasAttribute("branch"):
                # print application.getAttribute("branch")
                appInfo["branch"] = application.getAttribute("branch")
            # print appInfo
            appInfos.append(appInfo)

        # get libs info
        self.libs = self.collection.getElementsByTagName("lib")
        for lib in self.libs:
            libInfo = {}
            if lib.hasAttribute("addr"):
                # print lib.getAttribute("addr")
                libInfo["addr"] = lib.getAttribute("addr")
            if lib.hasAttribute("path"):
                # print lib.getAttribute("path")
                libInfo["path"] = lib.getAttribute("path")
            if lib.hasAttribute("branch"):
                # print lib.getAttribute("branch")
                libInfo["branch"] = lib.getAttribute("branch")
            # print libInfo
            appInfos.append(libInfo)

        # print appInfos
        return appInfos

    pass


# git clone submodule
class gitUtil():
    def __init__(self, rootpath):
        # self.pwd = os.getcwd().replace("\n", "")
        self.pwd = rootpath
        print self.pwd
        pass

    def cloneSubmodule(self, appInfos):
        print 'Start git clone submodule...'
        for i in range(len(appInfos)):
            pwd = self.pwd + '/' + appInfos[i]["path"]
            if os.path.exists(pwd):
                print pwd
                shutil.rmtree(pwd)
            os.makedirs(pwd)
            if appInfos[i].has_key("branch"):
                os.system("git clone -b " + appInfos[i]["branch"] + " " + appInfos[i]['addr'] + " " + pwd)
            else:
                os.system("git clone " + appInfos[i]['addr'] + " " + pwd)
        print 'Clone is complete, enjoy of coding...'

    pass

    def pullSubmodule(self, appInfos):
        print 'Start git pull submodule...'
        for i in range(len(appInfos)):
            pwd = self.pwd + '/' + appInfos[i]["path"]
            if os.path.exists(pwd):
                os.chdir(pwd)
                print os.getcwd().replace("\n", "")
                if appInfos[i].has_key("branch"):
                    os.system("git pull origin " + appInfos[i]["branch"])
                else:
                    os.system("git pull")
        print 'Pull is complete, enjoy of coding...'
        pass

    def lsSubmodule(self, appInfos):
        print 'Start git ls submodule...'
        for i in range(len(appInfos)):
            pwd = self.pwd + '/' + appInfos[i]["path"]
            if os.path.exists(pwd):
                os.chdir(pwd)
                print os.getcwd().replace("\n", "")
                os.system("git branch -a")
        print 'ls is complete, enjoy of coding...'
        pass

    def cmdSubmodule(self, appInfos, cmd):
        for i in range(len(appInfos)):
            pwd = self.pwd + '/' + appInfos[i]["path"]
            if os.path.exists(pwd):
                os.chdir(pwd)
                print os.getcwd().replace("\n", "")
                os.system(cmd)
        pass


def usage():
    print "Usage:"
    print "     clone    Init lyra project group by manifest.xml"
    print "     pull     Pull all submodule from remote branch"
    print "     help     Just above"


if __name__ == '__main__':
    paras = {}
    action = None
    val = None
    val2 = None
    val3 = None
    argv = []
    for i in range(0, len(sys.argv)):
        v = sys.argv[i]
        if v != '-G' and v != '-i':
            argv.append(v)
    if IS_DEBUG:
        print argv
    if (len(argv) > 1):
        action = argv[1]
    if (len(argv) > 2):
        val = argv[2]
    if (len(argv) > 3):
        val2 = argv[3]
    if (len(argv) > 4):
        val3 = argv[4]

    if IS_DEBUG:
        print "input para: action=%s,val=%s,val2=%s,val3=%s" % (action, val, val2, val3)
    shpath = os.path.dirname(argv[0])
    macos = ("Darwin" in cmd('uname')[0])
    # print "macos " macos
    osname = ('mac' if macos else 'ubuntu')
    configpath = shpath + '/' + "../../../config/%s/lyra_auto.json" % (osname)
    cfgstr = open(configpath).read()
    cfg = json.loads(cfgstr)
    rootpath = cfg['root_path']
    innerapps = ['aios', 'launcher', 'wechat', 'music', 'dialog']

    if len(sys.argv) >= 1:
        xmlUtil = xmlUtil(rootpath + "/manifest.xml")
        appInfos = xmlUtil.parseXml()

        gitUtil = gitUtil(rootpath)
        if sys.argv[1] == "clone":
            gitUtil.cloneSubmodule(appInfos)
        elif sys.argv[1] == "pull":
            gitUtil.pullSubmodule(appInfos)
        elif sys.argv[1] == "ls":
            gitUtil.lsSubmodule(appInfos)
        elif action == "cmd":
            print "exe cmd"
            gitUtil.cmdSubmodule(appInfos, val)
        elif sys.argv[1] == "help":
            usage()
        else:
            print "The command is not supported, you can see below"
            usage()
    else:
        usage()
