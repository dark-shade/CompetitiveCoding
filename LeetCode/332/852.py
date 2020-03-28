from typing import List
"""
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) < 3:
            return -1

        prev_num = A[0]
        
        for i, n in enumerate(A):
            if prev_num > n:
                return i - 1
            prev_num = n

        return -1
"""

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if len(A) < 3:
            return -1
        
        lo = 0
        hi = len(A) - 1

        while lo < hi:
            mid = int((lo + hi) / 2)
            if A[mid] < A[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
            
        return lo

obj = Solution()
n = obj.peakIndexInMountainArray([0,2,1,0])
print(n)
