from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # create m by n matrix
        matrix = []

        for _ in range(n):
            matrix.append([0] * m)

        # oddCells logic
        for indice in indices:
            for i in range(len(matrix[indice[0]])):
                matrix[indice[0]][i] += 1
            
            for row_id in range(len(matrix)):
                matrix[row_id][indice[1]] += 1

        odd_cnt = 0

        for row in matrix:
            for num in row:
                if num % 2 != 0:
                    odd_cnt += 1

        return odd_cnt