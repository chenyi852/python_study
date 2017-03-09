#!/usr/bin/env python
#coding=utf-8

import os
import shutil
import filecmp
dl_path=r'E:\BaiduYunDownload'
msc_path=r'E:\music'

def endwith(*endstring):
	ends = endstring
	def run(s):
		f = map(s.endswith,ends)
		if True in f: return s
	return run

def rm_suffix(item):
	file=item.replace("[mqms2](1)", "")
	new=file.replace("[mqms2]", "")
	nfile=new.replace(' ', '')
	return nfile
	
def cp_download(src_path, dst_path):
	files=filecmp.dircmp(src_path, dst_path).left_only
	a=endwith('.mp3','.flac', 'm4a', 'ape')
	f_files=filter(a, files)
	
	for item in f_files:
		file=rm_suffix(item)
		src_file=src_path + '\\' + item
		dst_file=dst_path + '\\' + file
		if  not ((os.path.isdir(src_file)) or (os.path.exists(dst_file))):
			print "copy " + src_file +" to " + dst_file
			shutil.move(src_file, dst_file)
		
	
	
	
if __name__ == "__main__":
	cp_download(dl_path, msc_path)
	