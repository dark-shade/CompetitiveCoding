from typing import List

"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_negative = 0
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell < 0:
                    num_negative += 1

        return num_negative
"""

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        num_negative = 0
        m = len(grid[0])

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell < 0:
                    num_negative += (len(grid) - i) * (m - j)
                    m = j
                    break

        return num_negative


                
obj = Solution()
n = obj.countNegatives([[1,-1],[-1,-1]])
print(n)
