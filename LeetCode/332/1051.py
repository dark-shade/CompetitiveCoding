from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        cnt = 0

        for i, height in enumerate(heights):
            if height != sorted_heights[i]:
                cnt += 1
        
        return cnt
        