from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            if i % 2 != 0:
                continue
                
            temp_list = [nums[i + 1]] * nums[i]
            result += temp_list

        return result
            
obj = Solution()
d = obj.decompressRLElist([1,1,2,3])
print(d)
