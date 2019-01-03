#!/usr/bin/env python
# -*- coding:utf-8-*-

import os
import hashlib


target_dir="/home/chenyi/音乐"

def filecount():
    command = 'ls -lR ' + target_dir + '| grep "^-" | wc -l'
    print ('the command to be executed is : ', command)
    filecount = os.popen(command).read()
    return int(filecount)

def md5sum(filename):
    f = open(filename, 'rb')
    md5 = hashlib.md5()
    while True:
        fb = f.read(8096)
        if not fb:
            break
        md5.update(fb)
    f.close()
    return (md5.hexdigest())

def delfile():
    all_md5={}
    filedir = os.walk(target_dir)
    for root, dirs, files in filedir:
        for tlie in files:
            path=os.path.join(root, tlie)
            if md5sum(path) in all_md5.values():
                os.remove(path)
                print('remove', path)
            else:
                all_md5[tlie] = md5sum(path)

if __name__ == '__main__':
    oldf = filecount()
    print('the file count before redundant files removed', oldf)
    delfile()
    print('After removing redundant files, there are only', filecount(), 'files')
    print(oldf - filecount() + ' files has been removed')
