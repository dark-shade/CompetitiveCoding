class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if len(nums) >= k:
            self.nums = sorted(nums)[len(nums)-k:]
        else:
            self.nums = sorted(nums)

    def add(self, val: int) -> int:
        self.nums = sorted(self.nums + [val])
        
        if len(self.nums) > self.k:
            self.nums.pop(0)
            
        return self.nums[0]
                        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)