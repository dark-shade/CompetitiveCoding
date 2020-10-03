"""TLE
class Solution:
    def minMoves(self, nums: List[int]) -> int:        
        min_num, max_num, max_index = self.getMinMax(nums)
        moves = 0
        
        
        while min_num != max_num:
            cnt = max_num - min_num
            moves += cnt 
            
            for i in range(len(nums)):
                if i != max_index:
                    nums[i] += cnt
            
            min_num, max_num, max_index = self.getMinMax(nums)
            
        return moves        
        
    def getMinMax(self, nums: List[int]) -> List[int]:
        # min, max, max_index
        values = [-1]*3
        
        for i in range(len(nums)):
            if values[0] == -1 or values[0] > nums[i]:
                values[0] = nums[i]
                
            if values[1] == -1 or values[1] < nums[i]:
                values[1] = nums[i]
                values[2] = i
                
        return values
"""
"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        moves = 0
        max_num = nums[-1]
        min_num = nums[0]
        
        while nums[0] != nums[-1]:
            moves += nums[-1] - nums[0]
            nums[len(nums)-2] += moves
            nums = nums[-1:] + nums[:len(nums)-1]
            
        return moves              
"""
"""344 ms 15.1 MB
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        nums.sort()
        moves = 0
        max_num = nums[-1]
        min_num = nums[0]
        ind = len(nums) - 2
        
        while max_num != min_num:
            moves += max_num - min_num
            min_num = max_num
            max_num = nums[ind] + moves
            ind -= 1
            
        return moves
"""