#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import sys
import re
import shutil

path="/home/chenyi/音乐"
windows_path="D:\03_personal\01_music"
cygwin_path="/cygdrive/d/03_personal/01_music"

def modify_name(file_path):
    list_file = os.listdir(file_path)
    for item in list_file :
    #将文件名中"[mqms2](1)"去掉
        filename=file_path + '/' + item

        newname=re.sub(r'\[\w*\]\(*\d*\)*', "", filename)
        print("%s --> %s" %(filename, newname))
        """
	    ewname=filename.replace("[mqms2](1)", '')
	    newname=newname.replace("[mqms2]", '')
	    newname=newname.replace("[mqms]", '')
	    newname=newname.replace(' ', '')
	"""
        if not (os.path.normcase(filename) == os.path.normcase(newname)):
            print ("move " + filename + "to " + newname)
            shutil.move(filename, newname)

def cleanup_filename(myfile):
    new = re.sub(r'\[\w*\]\(*\d*\)*', "", myfile)
    print("file is %s, new file name is %s" %(myfile, new))

if __name__ == '__main__':
    if os.path.exists(path):
        print("%s exists" %(path))
        modify_name(path)
    if os.path.exists(windows_path):
        print("%s exists" %(windows_path))
        modify_name(windows_path)
    if os.path.exists(cygwin_path):
        print("%s exists" %(cygwin_path))
        modify_name(cygwin_path)
    """ 
        for test
	cleanup_filename("my[mqms2].mp3")
	cleanup_filename("my[mqms2](1).mp3")
	cleanup_filename("my[mqms].mp3")
    """
