from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        greater_num = len(S)
        smaller_num = 0

        final_list = []

        for i, ch in enumerate(S):
            if ch == "I":
                if len(final_list) == 0:
                    final_list.append(smaller_num)
                    smaller_num += 1
                if final_list[-1] < smaller_num:
                    final_list.append(smaller_num)
                    smaller_num += 1
            else:
                if len(final_list) == 0:
                    final_list.append(greater_num)
                    greater_num -= 1
                if final_list[-1] > smaller_num:

                final_list.append(smaller_num)
                smaller_num += 1
            
        return final_list

obj = Solution()
fl = obj.diStringMatch("DDI")
print(fl)
