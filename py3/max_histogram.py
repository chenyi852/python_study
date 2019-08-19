#!/usr/bin/env python
#coding:utf-8

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: list[int]
        :rtype int
        """
        i = 0
        stack = []
        max_value = 0

        while (i < len(heights)):
            if len(stack) == 0 or heights[stack[-1]] < heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                max_value = max(max_value, heights[top] * ((i - stack[-1] - 1 ) if stack else i ))

        while  stack:
            top = stack.pop()
            max_value =  max(max_value, heights[top] * ((i - stack[-1] - 1) if stack else i))

        return max_value

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    x = Solution()
    print("max area is %d" %(x.largestRectangleArea(heights)))
