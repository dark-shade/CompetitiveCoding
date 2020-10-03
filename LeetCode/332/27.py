""" 32 ms
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                for j in range(i+1, len(nums)):
                    if nums[j] != val:
                        cnt += 1
                        nums[i] = nums[j]
                        nums[j] = val
                        break
            else:
                cnt += 1
        print(cnt)
        return cnt
"""
""" 28 ms
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v = 0
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[v] = nums[i]
                v += 1
        
        return v
"""
