from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_set = set()

        for n in nums1:
            if n in nums2:
                final_set.add(n)
        
        return list(final_set)
