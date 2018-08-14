#!/usr/bin/env python
# coding=utf-8

import math
import sys
str='helloworld'
print(str)
print("this lenth of (%s) is (%d)" %(str, len(str)))

nhex=0xff
print("nhex=%x, ndec=%d, noct=%o" %(nhex, nhex, nhex))


## float
print("PI=%f, PI=%10.3f, PI=%06d" %(math.pi, math.pi, math.pi))

## string
print("%.3s" %(str))
print("%.*s" %(6,str))
print("%10.4s" %(str))

# list
lst=[1,2,3,4,'python']
print(lst)

# dictonary
d={1:'a',2:'b',3:'c',4:'d'}
print(d)

# new line
for i in range(0,6):
    print(i)

# usind system function directly
sys.stdout.write("hello world")
