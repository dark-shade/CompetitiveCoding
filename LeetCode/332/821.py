from typing import List

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        pos = []
        final_dist = []

        for i, ch in enumerate(S):
            if ch == C:
                pos.append(i)
        
        for i in range(len(S)):
            dist = self.getMin(pos, i)
            final_dist.append(dist)

        return final_dist

    def getMin(self, pos, curr_index):
        min = abs(pos[0] - curr_index)

        for p in pos:
            if abs(p - curr_index) < min:
                min = abs(p - curr_index)
        
        return min
