import collections

""" 48ms
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_col = collections.Counter(s)
        t_col = collections.Counter(t)
        
        for k in t_col - s_col:
            return k
            
        return ""
"""

""" 36 ms
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_col = collections.Counter(s)
        s_col += collections.Counter(t)
        
        for k in s_col:
            if s_col[k] % 2 != 0:
                return k
            
        return ""
"""