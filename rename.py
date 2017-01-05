#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import re
import shutil

path="/home/chenyi/音乐"

list_file = os.listdir(path)
for filename in list_file :
    #将文件名中"[mqms2](1)"去掉
    newname=filename.replace("[mqms2](1)", "")
    newname=newname.replace("[mqms2]", "")
    shutil.move(filename, newname)
