from typing import List

"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0 
        index2 = len(numbers) - 1

        while index1 < index2:
            num_sum = numbers[index1] + numbers[index2]
            if num_sum == target:
                break
            elif num_sum > target:
                index2 -= 1
            else:
                index1 += 1
            
        return [index1 + 1, index2 + 1]
"""
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            if (target - n) in numbers:
                return [i+1, numbers[i+1:].index(target - n) + i + 2]
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0 
        index2 = len(numbers) - 1

        while index1 < index2:
            num_sum = numbers[index1] + numbers[index2]
            if num_sum == target:
                break
            elif num_sum > target:
                if numbers[index1] + numbers[int(len(numbers[index1:index2])/2)] > target:
                    index2 = int(len(numbers[index1:index2])/2)
                else:
                    index2 -= 1
            else:
                if numbers[index1] + numbers[int(len(numbers[index1:index2])/2)] < target:
                    index2 = int(len(numbers[index1:index2])/2)
                else:
                    index1 += 1
            
        return [index1 + 1, index2 + 1]