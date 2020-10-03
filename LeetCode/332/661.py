class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        smooth = []
        
        for i in range(len(M)):
            row = []
            
            for j in range(len(M[0])):
                cnt = 1
                total = M[i][j]
                
                if i > 0:
                    total += M[i-1][j]
                    cnt += 1
                
                if i < len(M) - 1:
                    total += M[i+1][j]
                    cnt += 1
                    
                if j > 0:
                    total += M[i][j-1]
                    cnt += 1
                    
                if j < len(M[0]) - 1:
                    total += M[i][j+1]
                    cnt += 1
                    
                if i > 0 and j > 0:
                    total += M[i-1][j-1]
                    cnt += 1
                    
                if i > 0 and j < len(M[0]) - 1:
                    total += M[i-1][j+1]
                    cnt += 1
                    
                if i < len(M) - 1 and j > 0:
                    total += M[i+1][j-1]
                    cnt += 1
                    
                if i < len(M) - 1 and j < len(M[0]) - 1:
                    total += M[i+1][j+1]
                    cnt += 1
                    
                row.append(math.floor(total/cnt))
                
            smooth.append(row)
            
        return smooth