#!/usr/bin/env python
# coding=utf-8

import re
import urllib

from bs4 import BeautifulSoup

def bs_pic(url):
    img = urllib.urlopen(url).read()
    fhand = open('cover.jpg', 'w')
    fhand.write(img)
    fhand.close()

def bs_picx(url):
    img = urllib.urlopen(url)
    fhand = open('cover.jpg', 'w')
    size = 0

    while True:
        info = img.read(100*1024)
        if len(info) < 1:
            break
        size = size + len(info)
        fhand.write(info)

    print size, 'charatcters copied.'
    fhand.close()

def bs_test(url):
    lst = list()
    index = url.rfind('/')
    print index, "index\n"
    root_url = url[0:index+1]
    url = urllib.urlopen(url).read()
    soup = BeautifulSoup(url, 'html.parser')

    #Retrieve all of the anchor tags
    tags = soup('a')
    count = 0
    for tag in tags:
        #if re.search('[0-9]', tag.get('href', None)[:1]):
        if tag.get('href', None)[0].isnumeric():
            page = root_url + tag.get('href', None)
            lst.append(page)
            print page
        count += 1
        #print tag.get('href', None)
    print "count is : ", count
print "bs test"
#bs_pic('http://www.py4inf.com/cover.jpg')
#bs_picx('http://www.py4inf.com/cover.jpg')
bs_test('http://www.piaotian.com/html/7/7794/index.html')
