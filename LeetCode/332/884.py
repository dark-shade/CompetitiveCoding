from typing import List
import collections

"""
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a_ctr = collections.Counter(A.split())
        b_ctr = collections.Counter(B.split())
        
        final_l = []
        
        for w in a_ctr.keys():
            if a_ctr[w] == 1:
                if w not in b_ctr.keys():
                    final_l.append(w)
                    
        for w in b_ctr.keys():
            if b_ctr[w] == 1:
                if w not in a_ctr.keys():
                    final_l.append(w)
                    
        return final_l
"""
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        ctr = collections.Counter(A.split())
        ctr += collections.Counter(B.split())
                    
        return [w for w in ctr if ctr[w] == 1]