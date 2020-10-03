from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # of form {num: count}
        counter = {}

        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        for n in counter.keys():
            if counter[n] >= len(nums) / 2:
                return n
        