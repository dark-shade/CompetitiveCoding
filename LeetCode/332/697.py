""" 516 ms
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:        
        ctr = collections.Counter(nums)
        max_degree_nums = []
        max_degree = -1
        
        for k in ctr:
            if max_degree < ctr[k]:
                max_degree = ctr[k]
                max_degree_nums = []
                max_degree_nums.append(k)
            elif max_degree == ctr[k]:
                max_degree_nums.append(k)                
        
        # of form {num: [first_pos, last_pos]}
        positions = {}
        
        for i, n in enumerate(nums):
            if n in max_degree_nums:
                if n not in positions:
                    positions[n] = [i,i]
                else:
                    positions[n][1] = i
                    
        min_length = len(nums)
        
        
        
        for n in positions:
            length = positions[n][1] - positions[n][0] + 1
            
            if min_length > length:
                min_length = length
                
        return min_length
"""
"""256 ms
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:        
        # of form {num: [degree, first_index, last_index]}
        ctr = {}
        max_degree = -1
        max_degree_nums = []
        
        for i, n in enumerate(nums):
            if n not in ctr:
                ctr[n] = [1, i, i]
            else:
                ctr[n][0] += 1
                ctr[n][2] = i
                
            if ctr[n][0] > max_degree:
                max_degree = ctr[n][0]
                max_degree_nums = [n]
            elif ctr[n][0] == max_degree:
                max_degree_nums.append(n)
        
        min_length = len(nums)
        
        for n in max_degree_nums:
            length = ctr[n][2] - ctr[n][1] + 1
            
            if min_length > length:
                min_length = length
                
        return min_length
"""