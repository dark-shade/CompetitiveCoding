"""140 ms
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        
        cnt = 0
        curr = arr[0]
        
        for n in arr:
            if curr == n:
                cnt += 1
            else:
                if cnt > len(arr) / 4:
                    return curr
                
                curr = n
                cnt = 1
                
        return curr
"""
"""132 ms
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        
        ctr = collections.Counter(arr)
        
        for k in ctr:
            if ctr[k] > len(arr) / 4:
                return k
"""
"""100 ms
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        
        n = len(arr) // 4
        
        for i in range(len(arr)):
            if arr[i] == arr[i+n]:
                return arr[i]
"""