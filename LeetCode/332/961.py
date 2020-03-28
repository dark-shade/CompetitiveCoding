from typing import List

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        already = set()

        for n in A:
            if n in already:
                return n
            
            already.add(n)       


obj = Solution()
n = obj.repeatedNTimes([5,1,5,2,5,3,5,4])
print(n)
