"""344 ms
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        
        while low != high and mid >= 0 and mid < len(nums):
            mid = (low + high) // 2
            
            if target > nums[mid]:
                low = mid + 1
                
            elif target < nums[mid]:
                high = mid - 1
                
            else:
                return mid
            
        if nums[low] == target:
            return low
            
        return -1
"""
"""436 ms
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
                
            else:
                left = mid + 1
                
        return -1
"""
"""360 ms
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1
"""