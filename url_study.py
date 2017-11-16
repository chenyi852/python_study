#!/usr/bin/env python
# encoding=utf-8

import urllib
import re

from bs4 import BeautifulSoup

def urlib_test():
	counts = dict()
	fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
	for line in fhand:
		words = line.split()
		for word in words:
			counts[word] = counts.get(word, 0) + 1
		print counts

def url_re(url):
	html = urllib.urlopen(url).read()
	links = re.findall('href="(http://.*?)"', html)
	for link in links:
		print link
	
	
def bs_test(url):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	
	# Retrieve all of the anchor tags
	tags = soup('a')
	for tag in tags:
	   print tag.get('href', None)
	
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html, "html.parser")
	
	# Retrieve all of the anchor tags
	tags = soup('a')
	for tag in tags:
		# look at the parts of a tag
		print 'TAG:', tag
		print 'URL:', tag.get('herf', None)
		print 'Content:', tag.contents[0]
		print 'Attrs:', tag.attrs
	   
urlib_test()
url_re("http://www.dr-chuck.com/page1.htm")
url_re("http://www.py4inf.com/book.htm")
print "-----BeautifulSoup test---"
bs_test("http://www.py4inf.com/book.htm")