from typing import List
import collections

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = collections.Counter(arr1)
        final_arr = []

        for n in arr2:
            final_arr.extend([n] * counter[n])

        suffix = []

        for k in counter.keys():
            if k not in arr2:
                suffix.extend([k] * counter[k])
        
        suffix.sort()

        final_arr.extend(suffix)

        return final_arr

            