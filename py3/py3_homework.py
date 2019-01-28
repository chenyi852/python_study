#!/usr/bin/env python
# coding=utf-8

lst=[]

def print_lst(mlst):
    for i in range(len(mlst)):
        print (i, mlst[i])

for i in range(30):
    lst.insert(i, i)

#print_lst(lst)
print (lst)
## there are 30 people in total. every whose number is 9, then poplulated from
## the queue. After 15 guys are populated from the queue, then the game is 
## finished.
total=30
idx=0
nlst=[]
while total > 15:
    idx += 8
    idx %= total
    nlst.insert((30-total), lst[idx])
    lst.pop(idx)
    total -= 1
    print ("new list :", nlst)
    print ("original list :", lst)

