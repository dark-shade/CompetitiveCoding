"""72 ms
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        carry = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if carry + nums[i] > nums[i]:
                carry += nums[i]
            else:
                carry = nums[i]
                
            if carry > max_sum:
                max_sum = carry
                
        return max_sum
"""
