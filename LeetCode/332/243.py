from typing import List

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dist = 0
        ind_1 = -1
        ind_2 = -1

        for i, word in enumerate(words):
            if word == word1:
                ind_1 = i
                if ind_2 != -1:
                    if dist > abs(ind_1 - ind_2) or dist == 0:
                        dist = abs(ind_1 - ind_2)
            if word == word2:
                ind_2 = i
                if ind_1 != -1:
                    if dist > abs(ind_2 - ind_1) or dist == 0:
                        dist = abs(ind_2 - ind_1)

        return dist

