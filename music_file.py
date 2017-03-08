#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import re
import shutil
import filecmp

download_path=r'C:\Users\c00200500.CHINA\Downloads'
music_path=r'D:\03_personal\01_music'
path="/home/chenyi/音乐"

def endwith(*endstring):
	ends = endstring
	def run(s):
		f = map(s.endswith,ends)
		if True in f: return s
	return run
  
def rm_suffix(srcpath):
	list_file = os.listdir(srcpath)
	for item in list_file :
		#将文件名中"[mqms2](1)"去掉
		filename = srcpath + '\\' + item
		newname=filename.replace("[mqms2](1)", "")
		newname=newname.replace("[mqms2]", "")
		if not (os.path.exists(newname)):
			print "move " + filename + " to " + newname
			shutil.move(filename, newname)

def cp_download(src_path, dst_path):
	left_files=filecmp.dircmp(src_path,dst_path).left_only
	a = endwith('.mp3','.flac','.m4a', '.ape')
	f_files = filter(a, left_files)
	for item in f_files:
		src_file = src_path + '\\' + item
		dst_file = dst_path + '\\' + item
		if not (os.path.isdir(src_file)):
			# check if the file is exist, before move another file to this file.
			if not (os.path.exists(dst_file)):
				print "move {src} to {dst}" .format(src=src_file, dst=dst_file)
				shutil.move(src_file, dst_file)
				

			
if __name__ == "__main__":
	print "copy {src} to {dst}".format(src=download_path, dst=music_path)
	cp_download(download_path, music_path)
	rm_suffix(music_path)
