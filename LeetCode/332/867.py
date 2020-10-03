from typing import List

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        tp_A = []

        for j in range(len(A[0])):
            row = []
            for i in range(len(A)):
                row.append(A[i][j])
            tp_A.append(row)

        return tp_A
        