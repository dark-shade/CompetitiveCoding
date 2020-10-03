"""88 ms
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:        
        for i in range(len(nums)):
            if target == nums[i] or nums[i] > target:
                return i
            
        return len(nums)
"""