class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        front_ptr = 0 
        end_ptr = len(nums) - 1
        total_sum = 0

        cnt = len(nums)

        while cnt > 1:
            if total_sum > 0:
                total_sum -= nums[end_ptr]
                end_ptr -= 1
            else:
                total_sum += nums[front_ptr]
                front_ptr += 1
            cnt -= 1

        if total_sum == 0:
            return front_ptr

        return -1
