#!/usr/bin/env python
# coding=utf-8
import string

def tuple_test():
	d = {'a':10, 'b':1, 'c':22}
	t = list()
	for key, val in d.items():
		t.append((val, key))
	t.sort(reverse = True)
	print t

def largest_count(fname):
	try:
		fhand = open(fname)
	except:
		print "open %s fail" %fname
		
	counts = dict()
	
	for line in fhand:
		line = line.translate(None, string.punctuation)
		line = line.lower()
		words = line.split()
		for word in words:
			counts[word] = counts.get(word, 0) + 1
	t = list()
	for key, val in counts.items():
		t.append((val, key))
	t.sort(reverse = True)
		
	for key,val in t[:10]:
		print key, val
		
tuple_test()
largest_count('mbox.txt')