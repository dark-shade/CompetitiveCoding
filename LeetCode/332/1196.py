from typing import List

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()

        wt = 0
        cnt = 0

        for w in arr:
            if wt + w > 5000:
                break
            wt += w
            cnt += 1
        
        return cnt
