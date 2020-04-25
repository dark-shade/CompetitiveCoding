from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd_list = []
        even_list = []
        final_list = []

        for n in A:
            if n % 2 == 0:
                even_list.append(n)
            else:
                odd_list.append(n)

        for i in range(len(A)):
            if i % 2 == 0:
                final_list.append(even_list.pop())
            else:
                final_list.append(odd_list.pop())

        return final_list
