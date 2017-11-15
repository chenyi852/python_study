#!/usr/bin/env python
# encoding=utf-8

import socket
import time

def http_test():
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect(('www.py4inf.com', 80))
	mysock.send('GET /code/romeo.txt HTTP/1.0\r\nHost: www.py4inf.com\r\n\r\n')

	while True:
		data = mysock.recv(512)
		if ( len(data) < 1 ) :
			break
		print data
	
	mysock.close()
	
def http_picture():
	mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysock.connect(('www.py4inf.com', 80))
#	mysock.send('GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')
#Absolute is acceptable with HTTP/1.1 but you use HTTP/1.0.
	mysock.send('GET /cover.jpg HTTP/1.0\r\nHost:www.py4inf.com\r\n\r\n')


	count = 0
	picture = "";
	while True:
		data = mysock.recv(5120)
		if ( len(data) < 1 ) : break
		# time.sleep(0.25)
		count = count + len(data)
		print len(data),count
		picture = picture + data

	mysock.close()

	# Look for the end of the header (2 CRLF)
	pos = picture.find("\r\n\r\n");
	print 'Header length',pos
	print picture[:pos]

	# Skip past the header and save the picture data
	picture = picture[pos+4:]
	fhand = open("stuff.jpg","wb")
	fhand.write(picture);
	fhand.close()
		
http_picture()