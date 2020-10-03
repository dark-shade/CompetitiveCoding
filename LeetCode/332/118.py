""" 44 ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        
        triangle = [[1]]
        
        for r in range(1, numRows):
            row = []
            
            for i in range(r + 1):
                if i == 0:
                    row.append(1)
                    continue
                elif i == r:
                    row.append(1)
                    continue
                    
                row.append(triangle[r - 1][i] + triangle[r - 1][i - 1])
                
            triangle.append(row)
            
        
        return triangle
"""
""" 28 ms
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows < 1:
            return []
        
        triangle = [[1]]
        
        for r in range(1, numRows):
            row = []
            
            for i in range(r + 1):
                if i == 0:
                    row.append(1)
                    continue
                elif i == r:
                    row.append(1)
                    continue
                    
                row.append(triangle[r - 1][i] + triangle[r - 1][i - 1])
                
                if i >= int(r/2):
                    if r % 2 == 0:
                        row.extend(list(reversed(row[:i])))
                    else:
                        row.extend(list(reversed(row)))
                    break
                
            triangle.append(row)
            
        
        return triangle
"""