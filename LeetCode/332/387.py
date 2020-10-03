class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_cnt = collections.Counter(s)
        
        ch_index = -1
        
        for k in s_cnt:
            if s_cnt[k] == 1:
                char_index = s.index(k)
                if ch_index == -1:
                    ch_index = char_index
                elif char_index < ch_index:
                    ch_index = char_index
            
            
        return ch_index