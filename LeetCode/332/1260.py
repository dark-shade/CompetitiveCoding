class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:        
        grid_string = []
        
        for i in range(len(grid)):
            grid_string.extend(grid[i])
        
        k = k % len(grid_string)
        print(k)
        grid_string = grid_string[len(grid_string) - k:] + grid_string[:len(grid_string) - k]
        
        print(grid_string)
        
        itr = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = grid_string[itr]
                itr += 1
                
        return grid
        