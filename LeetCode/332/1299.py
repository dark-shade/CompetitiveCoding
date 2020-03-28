from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        final_list = []
        max_num = 0

        for n in arr[::-1]:
            if len(final_list) == 0:
                final_list.append(-1)
                max_num = n
                continue

            final_list = [max_num] + final_list

            if max_num < n:
                max_num = n

        return final_list

obj = Solution()
final_list = obj.replaceElements([17,18,5,4,6,1])
print(final_list)
            