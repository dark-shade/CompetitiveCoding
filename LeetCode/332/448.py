""" 568 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_ctr = collections.Counter(nums)
        missing = []
        
        for n in range(1, len(nums)+1):
            if n not in nums_ctr:
                missing.append(n)
                
        return missing
"""
""" 520 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        print(nums_set)
        return list(set([n for n in range(1, len(nums)+1)]) - nums_set)
"""
""" 496 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        return [n for n in range(1, len(nums) + 1) if n not in nums_set]
"""
""" 460 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = set()
        
        for n in range(1, len(nums) + 1):
            missing.add(n)
            
        nums_set = set(nums)
        
        for n in nums_set:
            missing.remove(n)
            
        return list(missing)
"""
""" 400 ms
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        da = [True for n in range(len(nums))]
        
        for n in nums_set:
            da[n - 1] = False
            
        return [i + 1 for i, b in enumerate(da) if b == True]
"""
