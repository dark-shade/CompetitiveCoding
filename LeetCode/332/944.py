from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        cnt = 0
        
        for i in range(len(A[0])):
            prev_char = ""

            for j in range(len(A)):
                if len(prev_char) == 0:
                    prev_char = A[j][i]
                    continue
                if A[j][i] < prev_char:
                    cnt += 1
                    break
                prev_char = A[j][i]

        return cnt
        