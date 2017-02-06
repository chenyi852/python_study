#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import re
import shutil

path="/home/chenyi/音乐"

def modify_name(file_path):
	list_file = os.listdir(file_path)
	for item in list_file :
		#将文件名中"[mqms2](1)"去掉
		filename = filepath + '\\' + item
		newname=filename.replace("[mqms2](1)", "")
		newname=newname.replace("[mqms2]", "")
		if not (os.path.normcase(filename) == os.path.normcase(newname)):
			print "move " + filename + "to " + newname
			shutil.move(filename, newname)

if __name__ == '__main__':
	modify_name(r'D:\03_personal\01_music')
	