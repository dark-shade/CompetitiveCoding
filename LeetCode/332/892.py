class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # row
                if i == 0:
                    area += grid[i][j]
                elif grid[i][j] > grid[i-1][j]:
                    area += grid[i][j] - grid[i-1][j]
                    
                if i == len(grid) - 1:
                    area += grid[i][j]
                elif grid[i][j] > grid[i+1][j]:
                    area += grid[i][j] - grid[i+1][j]
                
                # column
                if j == 0:
                    area += grid[i][j]
                elif grid[i][j] > grid[i][j-1]:
                    area += grid[i][j] - grid[i][j-1]
                    
                if j == len(grid[0]) - 1:
                    area += grid[i][j]
                elif grid[i][j] > grid[i][j+1]:
                    area += grid[i][j] - grid[i][j+1]
                    
                # top and bottom
                if grid[i][j] > 0:
                    area += 2
                    
        return area
                    
                    
                    