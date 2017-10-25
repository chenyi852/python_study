#!/usr/bin/env python
# coding=utf-8
import random


def random_test():
	print "----"
	for i in range(10):
		#x=random.random()
		x=random.randint(2,9)
	print x
	t=[1,2,3]
	print "choice :%d" %random.choice(t)


def computepay(hour, rate):
	try:
		if hours > 40 :
			pay = 40 * rate
			pay += (hours - 40) * rate*1.5

		print 'Pay:%.2f' %pay

	except:

		print "Error, please enter numeric input"

def while_test():
	n = 0
	while n < 5:
		print n
		n = n + 1

	while True :
		if n > 10:
			break;
		n = n + 1
		print n

def for_test():
	friends = ['chenyi', 'lilin', 'liuhong']
	for friend in friends:
		print 'Happy new year', friend
	print "done!"

	total = 0
	for itervar in [3,4,5,6,7]:
		total =total + itervar
	print "total : ", total

random_test()
#hours=float(raw_input("Enter Housr:"))
#rate=float(raw_input("Enter Rate:"))
#computepay(hours, rate)
while_test()
for_test()
