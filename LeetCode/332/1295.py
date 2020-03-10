from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0

        for n in nums:     
            if self.calcNumOfDigits(n) % 2 == 0:
                cnt += 1
        
        return cnt

    def calcNumOfDigits(self, num: int) -> int:
        cnt = 0

        while num > 0:
            num = int(num/10)
            cnt += 1
        
        return cnt
            
obj = Solution()
n = obj.findNumbers([12,345,2,6,7896])
print(n)
