#!/usr/bin/env python
# coding=utf-8
import re

def re_all(fname):
	s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting @2PM'
	lst = re.findall('\S+@\S+', s)
	print lst
	x = 'We just received $10.00 for cookies.'
	y = re.findall("\$[0-9.]+", x)
	print y
	
	count = 0
	try:
		fhand = open(fname)

	except:
		print "open %s fail" %fname

	for line in fhand:
		line = line.rstrip()
		x = re.findall("^X\S+: ([0-9.]+)", line)
		if len(x) > 0:
			count += 1
	print "match number is ", count
	fhand.close()
	
re_all("mbox.txt")