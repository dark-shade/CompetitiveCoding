from typing import List

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return []

        even_nums = []
        odd_nums = []

        for n in A:
            if n % 2 == 0:
                even_nums.append(n)
            else:
                odd_nums.append(n)
            
        even_nums.extend(odd_nums)

        return even_nums
