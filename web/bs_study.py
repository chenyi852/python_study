#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import urllib.request
import chardet
import sys

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

	print (size, 'charatcters copied.')	
	fhand.close()

def bs_test(url):
	lst = list()
	index = url.rfind('/')
	print (index, "index\n")
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
			print (page)
		count += 1
		#print tag.get('href', None)
	print ("count is : ", count)

def processText(webpage):
	# EMPTY LIST TO STORE PROCESSED TEXT

	html = urllib.request.urlopen(webpage).read()   
	encoding  = chardet.detect(html)
	print (encoding)

	soup = BeautifulSoup(html, 'html.parser') 
	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()	# rip it out
		
	text = soup.get_text()
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	#print text
	titleUni = text.decode("GB18030", "ignore")
	print (titleUni)
	fhand = open("touxiang.txt", 'w')
	fhand.write(titleUni)
	fhand.close()
	
	
	
print ("bs test")
print (sys.getdefaultencoding())
#reload(sys) 
#sys.setdefaultencoding('utf8')  
print (sys.getdefaultencoding())
#bs_pic('http://www.py4inf.com/cover.jpg')
#bs_picx('http://www.py4inf.com/cover.jpg')
#bs_test('http://www.piaotian.com/html/7/7794/index.html')
processText("http://www.google.com")
#processText('http://www.piaotian.com/html/7/7794/4671004.html')
#processText('http://blog.csdn.net/hfahe/article/details/5494895')