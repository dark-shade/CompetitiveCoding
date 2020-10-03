from typing import List

"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dist = {}
        
        for i in range(R):            
            for j in range(C):
                dist[str(i) + "," + str(j)] = abs(i - r0) + abs(j - c0)
            
        final_coor = []
        for k, v in sorted(dist.items(), key=lambda item: item[1]):
            final_coor.append([int(k.split(',')[0]), int(k.split(',')[1])])
            
        return final_coor           
"""
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:        
        fringe = [[r0, c0]]
        visited = []
        
        while fringe:
            curr = fringe.pop(0)
            visited.append(curr)
            
            if curr[0] - 1 > -1 and [curr[0] - 1, curr[1]] not in visited and [curr[0] - 1, curr[1]] not in fringe:
                fringe.append([curr[0] - 1, curr[1]])
                
            if curr[0] + 1 < R and [curr[0] + 1, curr[1]] not in visited and [curr[0] + 1, curr[1]] not in fringe:
                fringe.append([curr[0] + 1, curr[1]])
        
            if curr[1] - 1 > -1 and [curr[0], curr[1] - 1] not in visited and [curr[0], curr[1] - 1] not in fringe:
                fringe.append([curr[0], curr[1] - 1])
                
            if curr[1] + 1 < C and [curr[0], curr[1] + 1] not in visited and [curr[0], curr[1] + 1] not in fringe:
                fringe.append([curr[0], curr[1] + 1])
                
        return visited