#!/usr/bin/python
#coding:utf-8

__metaclass__=type	#new style classs

class person:
	def __init__(self, name):
		self.name = name
	
	def get_name(self):
		return self.name
		
	def set_height(self,height):
		print "person set height : {height}" .format(height=height)
		
class girl(person):
	def __init__(self, name):
		super(girl, self).__init__(name) # need to deliver the paramenter to base class
		self.breast=90
		self.__name=name #private variable value
	
	#@property
	def get_personal_name(self):
		print "my name is : {name}" .format(name=self.__name)
		
	def set_height(self, height):
		self.height=height
		
	def get_height(self):
		return self.height
		
	def about(self):
		print "this girl's breat is {breast}, heigh is {height}" .format(breast=self.breast, height=self.height)
if __name__ == '__main__':
	cang = person('cang')
	cang.set_height(13)
	mali = girl('mali')
	mali.get_personal_name()
	name = mali.get_name()
	print "the person name is : {name}"  .format(name=name)
	
	mali.set_height(19)
	height = mali.get_height()
	print "mali height is : {height}" .format(height=height)
	
	mali.about()