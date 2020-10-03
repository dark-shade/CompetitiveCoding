import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ctr = collections.Counter(s)
        t_ctr = collections.Counter(t)

        if s_ctr == t_ctr:
            return True

        return False