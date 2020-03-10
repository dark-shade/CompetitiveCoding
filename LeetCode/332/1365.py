from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        
        sorted_nums = sorted(nums)

        for n in nums:
            result.append(sorted_nums.index(n))
        
        return result

obj = Solution()
c = obj.smallerNumbersThanCurrent([7,7,7,7])
print(c)
        