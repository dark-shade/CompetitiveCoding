from typing import List

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_num = min(A)
        sum_min = 0

        while min_num > 0:
            sum_min += min_num % 10
            min_num = int(min_num / 10)

        if sum_min % 2 != 0:
            return 0

        return 1

obj = Solution()
n = obj.sumOfDigits([99,77,33,66,55])
print(n)
