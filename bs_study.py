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

print "bs test"
#bs_pic('http://www.py4inf.com/cover.jpg')
bs_picx('http://www.py4inf.com/cover.jpg')
