"""276 ms 15.1 MB
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        if nums[1] < 0 and nums[0] * nums[1] * nums[-1] > nums[-3] * nums[-2] * nums[-1]:
            return nums[0] * nums[1] * nums[-1]
        
        return nums[-3] * nums[-2] * nums[-1]         
"""
"""268 ms 15 MB
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        n1,n2,p1,p2,p3 = float('inf'),float('inf'),float('-inf'),float('-inf'),float('-inf')
        
        for n in nums:
            if n > p3:
                p1 = p2
                p2 = p3
                p3 = n
            elif n > p2:
                p1 = p2
                p2 = n
            elif n > p1:
                p1 = n
                
            if n < n2:
                n1 = n2
                n2 = n
            elif n < n1:
                n1 = n
                
        return max(p1*p2*p3, p3*n1*n2)
"""