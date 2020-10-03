class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        
        row_min = ops[0][0]
        col_min = ops[0][1]
        
        for i in range(len(ops)):
            if ops[i][0] < row_min:
                row_min = ops[i][0]
                
            if ops[i][1] < col_min:
                col_min = ops[i][1]
                
        return row_min * col_min