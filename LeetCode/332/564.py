class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)
        
        max_sub = 0
        sub_length = 0
        
        for n in ctr:
            sub_length = 0
            
            if n - 1 in ctr:
                sub_length = ctr[n] + ctr[n-1]
                
            if sub_length > max_sub:
                max_sub = sub_length
                
            if n + 1 in ctr:
                sub_length = ctr[n] + ctr[n+1]
            
            if sub_length > max_sub:
                max_sub = sub_length
            
        return max_sub
                    