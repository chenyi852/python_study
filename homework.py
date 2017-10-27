#!/usr/bin/env python
# coding=utf-8
import random
import string

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

def str_test(fruit):
	print fruit[0:len(fruit)]
	print "empty: ", fruit[:]

	print 'index of a in the %s from third letter : ' %fruit, fruit.find('a', 3)
	index = len(fruit)
	while index > 0:
		index = index - 1
		print fruit[index]

def find_test():
	 data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
	 atpos = data.find('@')
	 sppos = data.find(' ', atpos)
	 host  = data[atpos + 1 : sppos]
	 print host

	 str = 'X-DSPAM-Confidence:  0.8475'
	 sppos = str.find(' ')
	 num  = str[sppos + 1 :]
	 print "number is %.2f" %float(num)

def file_count(filename):
	try :
		fhand = open(filename)
	except:
		print "%s can't be opened" %filename
		exit()
	count = 0
	weeks = dict()
	for line in fhand:    
		count = count + 1
		if line.lower().startswith('from:') and line.find('edu') == -1:
			line.rstrip()
			t = line.split()
			print t[1]
	print "%s has %d line" %(filename, count)
	fhand.close()

def listtable_test(t):

	for i in range(len(t)):
		t[i] = t[i] * 2

		print t[i]
	print "max one is %d : " %max(t)
	t.pop(1)
	del t[len(t) - 1]
	#mylist.remove(6)
	mylist.sort()
	print mylist

def dict_test():
	word = 'brontosaurus'
	d = dict()
	for c in word:
		d[c] = d.get(c, 0) + 1
	print d
	for key in d:
		print key, d[key]
		
		
def dict_file_test(fname):
	try:
		fhand = open(fname)
	except:
		print "%s can't open" %fname
		exit()
	counts = dict()
	for line in fhand:
		line = line.translate(None, string.punctuation)
		line = line.lower()
		# dict to list
		words = line. split()
		for word in words:
			# get retrurn default value/0 if word is not in counts
			counts[word] = counts.get(word, 0) + 1
	print counts

def file_count(filename):
	try :
		fhand = open(filename)
	except:
		print "%s can't be opened" %filename
		exit()
	count = 0
	weeks = dict()
	for line in fhand:    
		count = count + 1
		if line.lower().startswith('from') and line.lower().find('from:') == -1:
			line.rstrip()
			t = line.split(' ')
			weeks[t[2]] = weeks.get(t[2], 0) + 1
	print weeks
	for key in weeks:
		print key, weeks[key]
	print max(weeks)		
	print "%s has %d line" %(filename, count)
	fhand.close()
	

def week_count(filename):
	try :
		fhand = open(filename)
	except:
		print "%s can't be opened" %filename
		exit()
	count = 0
	weeks = {'Wed': 0, 'Sun': 0, 'Fri': 0, 'Thu': 0, 'Mon': 0, 'Tue': 0, 'Sat': 0}
	for line in fhand:    
		count = count + 1
		if line.lower().startswith('from') and line.lower().find('from:') == -1:
			line.rstrip()
			t = line.split(' ')
			if t[2] in weeks :
				weeks[t[2]] += 1
	print weeks
	for key in weeks:
		print key, weeks[key]
	#find the maximun of the dict
	print max(weeks.keys(), key=(lambda k: weeks[k]))		
	print "%s has %d line" %(filename, count)
	fhand.close()
	

def max_account(fname):
	try:
		fhand = open(fname)
	except:
		print "%s can't be opened" %fname
		exit()
	weeks = dict()	
	account = 0
	
	for line in fhand:
		if line.lower().startswith('from') and line.lower().find('from:') == -1:
			line.rstrip()
			t=line.split()
			account = t[1]
			weeks[account] = weeks.get(account, 0) + 1
			
	account = max(weeks.keys(), key=(lambda k: weeks[k]))
	name, domain = account.split('@')
	print domain
	print account, weeks[account]	

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
	
random_test()
#hours=float(raw_input("Enter Housr:"))
#rate=float(raw_input("Enter Rate:"))
#computepay(hours, rate)
while_test()
for_test()
str_test("banana")
find_test()
file_count("mbox.txt")
mylist = [6,2,3,4]
listtable_test(mylist)
dict_test()
dict_file_test("memo.txt")
max_account("mbox.txt")
tuple_test()
largest_count('mbox.txt')