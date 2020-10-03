"""40 ms
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = collections.Counter(nums)
        
        if target in cnt and cnt[target] > int(len(nums)/2):
            return True
            
        return False
"""
""" 32 ms
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = 0
        length = len(nums)
        
        for n in nums:
            if n == target:
                cnt += 1
                
            if cnt > int(length/2):
                return True
            
        return False
"""