#!/usr/bin/env python3

import math
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

## two non-empty link listes are given to represent two non-negative integers.
## Among them, their respective digits are stored in reverse order, and each
## node of them can only store one digit.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        val1 = self.caculate_val_of_list(l1)
        val2 = self.caculate_val_of_list(l2)

        sum = val1 + val2
        sum = int(sum)
     
        sum = str(sum)[::-1]

        res = [ListNode(int(ch)) for ch in sum]
        
        for i in (range(len(res) - 1)):
            res[i].next = res[i + 1]
        return res[0]
        
    def caculate_val_of_list(self, l: ListNode)->int:
        
        idx = 0
        num= 0
        while l:
            num += l.val * math.pow(10, idx)
            idx += 1
            l = l.next
        return num
            
if __name__ == "__main__":
#(2 -> 4 -> 3) + (5 -> 6 -> 4)

    x1 = ListNode(2)
   
    x2 = ListNode(4)
    x3 = ListNode(3)
    x1.next = x2
    x2.next = x3
    
    x4 = ListNode(5)
    x5 = ListNode(6)
    x6 = ListNode(4)
    x4.next = x5
    x5.next = x6
    x = Solution()
    res = x.addTwoNumbers(x1, x4)
    while res:
        print(res.val)
        res = res.next