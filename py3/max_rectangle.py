#!/usr/bin/env python

class Solution:
    def maximalRectangle(self, matrix) -> int:
        """
        :type matrix: list[list[str]]
        :rtype int
        """
        # len for row
        n = len(matrix)
        if n == 0:
            return n
        # len for column
        m = len(matrix[0])
        self.ans = 0
        
        heights = [0] * (m + 1)
        for i in range(n):
            for j in range(m):
             
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
             
            self.ans = max(self.ans, self.robot(heights))
             
        return self.ans
        
    def robot(self, heights):
        i = 0
        stack = []
        max_area = 0
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                max_area = max(max_area, heights[top] * ((i - 1 - stack[-1]) if stack else i))
         
        while stack:
            top = stack.pop()
            max_area = max(max_area, heights[top] * ((i - 1 - stack[-1]) if stack else i))
        
        return max_area
       
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]        
matrix=[]
matrix=[
    ["0","1"],
    ["1","0"]
]
x = Solution()
print("max area is %d" %(x.maximalRectangle(matrix)))
