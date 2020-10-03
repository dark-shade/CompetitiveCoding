from typing import List

class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i, n in enumerate(A):
            if i == n:
                return i
            
        return -1