from typing import List

class Solution:
    def __init__(self):
        self.mem = []

    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            self.mem.append([])
            for _ in range(len(grid[i])):
                self.mem[i].append(-1)

        return self.minPathCost(0, 0, grid)

    def minPathCost(self, x, y, grid):
        if x >= len(grid) or y >= len(grid[0]):
            if (x == len(grid)-1 and y == len(grid[0])) or (x == len(grid) and y == len(grid[0])-1):
                return 0
            else:
                return 9999

        if self.mem[x][y] == -1:
            self.mem[x][y] = min(self.minPathCost(x+1, y, grid), self.minPathCost(x, y+1, grid)) + grid[x][y]  

        return self.mem[x][y]

obj = Solution()
print(obj.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))