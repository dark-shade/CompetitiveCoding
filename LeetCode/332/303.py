"""1216 ms 17.2 MB
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
"""
"""1192 ms 18.8 MB
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.stored = {}

    def sumRange(self, i: int, j: int) -> int:
        if (i,j) in self.stored:
            return self.stored[(i,j)]
        
        sum_indices = sum(self.nums[i:j+1])
        self.stored[(i,j)] = sum_indices
            
        return sum_indices


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
"""
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * (len(nums) + 1)
                
        for i in range(len(nums)):
            self.sums[i+1] = self.sums[i] + nums[i]

    def sumRange(self, i: int, j: int) -> int:            
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)