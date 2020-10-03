from typing import List

"""
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()

        diff = A[-1] - A[0]

        if diff <= 2 * K:
            return 0

        return diff - 2 * K
"""
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)