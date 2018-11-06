#!/usr/bin/env python
# conding=utf-8

import re
import sys

def re_test(fname):
    try:
        fhand = open(fname)
    except:
        print ("open %s fail" %(fname))
        exit()
    for line in fhand:
        if re.search('^F..m', line):
            print (line)

def findall_test(fname):
    try:
        fhand = open(fname)
    except:
        print ("open %s fail" %(fname))
        exit()
    for line in fhand:
        line = line.rstrip()
        lst = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', line)
        if len(lst) > 0:
            print (lst)

'''
def find_book(fname):
	try:
		fhand = open(fname)
	except:
		print ("open %s fail" %(fname))
		exit()

	for line in fhand:
		line = line.rstrip()
		lst = re.findall('as', line)
	print (lst)
'''
def find_book(fname):
    try:
        fhand = open(fname)
    except:
        print ("open %s fail!" %(fname))
        exit()

    for line in fhand:
        ## rstrip 删除string末尾的字符，默认为空格
        line = line.rstrip()
        print (line)

#reload(sys)
#sys.setdefaultencoding('utf8')

re_test("mbox.txt")
#findall_test("mbox.txt")
print ("====下面为安全图书清单=====")
find_book('booklist.txt')
#print re.match(ur"[\u4e00-\u9fa5]+","��")
