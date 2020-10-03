from typing import List

"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        for i in range(len(nums)):
            if nums[i] == 0:
                for j in range(i+1, len(nums)):
                    if nums[j] != 0:
                        nums[i] = nums[j]
                        nums[j] = 0
                        break
"""
"""
# not working, will need mods
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Do not return anything, modify nums in-place instead.
        zero_ptr = 0
        non_zero_ptr = 0
        print(len(nums))
        while non_zero_ptr < len(nums) and zero_ptr < len(nums):
            if nums[non_zero_ptr] != 0 and nums[zero_ptr] == 0 and zero_ptr > non_zero_ptr:
                break

            if zero_ptr > -1 and zero_ptr < len(nums) and non_zero_ptr < len(nums) and zero_ptr < non_zero_ptr and nums[zero_ptr] == 0 and nums[non_zero_ptr] != 0:
                nums[zero_ptr] = nums[non_zero_ptr]
                nums[non_zero_ptr] = 0

            if non_zero_ptr < len(nums) and nums[non_zero_ptr] == 0:
                non_zero_ptr += 1
            
            if (zero_ptr < len(nums) and nums[zero_ptr] != 0) or zero_ptr == -1:
                zero_ptr += 1
            print("z = ", zero_ptr)
            print("nz = ", non_zero_ptr)
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        non_zero_list = []
        
        for num in nums:
            if num != 0:
                non_zero_list.append(num)

        for i in range(len(non_zero_list)):
            nums[i] = non_zero_list[i]

        for i in range(len(non_zero_list),len(nums)):
            nums[i] = 0

        
            