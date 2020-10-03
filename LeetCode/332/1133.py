from typing import List

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        count = {}
        
        for n in A:
            if n not in count:
                count[n] = 1
                continue
            count[n] += 1
            
        max_num = -1
        
        for k in count.keys():
            if count[k] == 1 and max_num < k:
                max_num = k                 
        
        return max_num