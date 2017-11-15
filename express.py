#!/usr/bin/env python
# conding=utf-8

import re

def re_test(fname):
    try:
        fhand = open(fname)
    except:
        print "open %s fail" %fname
        exit()
    for line in fhand:
        if re.search('^F..m', line):
            print line

def findall_test(fname):
    try:
        fhand = open(fname)
    except:
        print "open %s fail" %fname
        exit()
    for line in fhand:
        line = line.rstrip()
        lst = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z0-9]', line)
        if len(lst) > 0:
            print lst

re_test("mbox.txt")
findall_test("mbox.txt")
