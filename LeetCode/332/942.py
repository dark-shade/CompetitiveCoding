from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        smaller_num = 0
        greater_num = len(S)

        final_seq = []

        for ch in S:
            if ch == "I":
                final_seq.append(smaller_num)
                smaller_num += 1
            else:
                final_seq.append(greater_num)
                greater_num -= 1
            
        return final_seq + [smaller_num]
            