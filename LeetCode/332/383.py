""" 48 ms
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_cnt = collections.Counter(ransomNote)
        m_cnt = collections.Counter(magazine)
        
        if r_cnt == (r_cnt & m_cnt):
            return True
        
        return False
"""
