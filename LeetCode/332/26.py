class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        curr = nums[0]
        ptr = 1
        cnt = 1
        
        
        for i in range(len(nums)):
            if nums[i] != curr:
                curr = nums[i]
                nums[ptr] = nums[i]
                ptr += 1
                cnt += 1
                
        return cnt
                
                
        