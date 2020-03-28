from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        final_list = []

        if n % 2 != 0:            
            final_list.append(0)
        else:
            final_list.append(1)

        while len(final_list) != n:
            if final_list[-1] > 0:
                final_list.append(-1 * final_list[-1])
            else:
                final_list.append(-1 * final_list[-1] + 1)

        return final_list

obj = Solution()
fl = obj.sumZero(5)
print(fl)
if sum(fl) == 0:
    print("yes")
else:
    print("no")
