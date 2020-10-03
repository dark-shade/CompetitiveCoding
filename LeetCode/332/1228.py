"""48 ms 14.1 MB
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = int((arr[-1] - arr[0])/len(arr))
        
        if d == 0:
            return arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1] + d:
                return arr[i-1] + d
            
        return 0
"""