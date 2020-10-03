class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ideal_sum = int(n * (n+1) / 2)
        
        actual_sum = sum(nums)
        
        return int(ideal_sum - actual_sum)