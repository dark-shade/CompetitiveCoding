class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        i = 1
        prev_row = []
        curr_row = [1,1]
        
        while i < rowIndex:
            prev_row = curr_row
            curr_row = []
            
            for j in range(len(prev_row)):
                if j == 0:
                    curr_row.append(1)
                    continue
    
                curr_row.append(prev_row[j] + prev_row[j-1])
        
            curr_row.append(1)
            
            i += 1
            
        return curr_row
            
            