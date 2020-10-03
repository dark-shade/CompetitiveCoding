class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        group = []
        curr = s[0]
        g_cnt = 0
        
        for ch in s:
            if ch == curr:
                g_cnt += 1
            else:
                group.append(g_cnt)
                curr = ch
                g_cnt = 1
        
        if g_cnt > 0:
            group.append(g_cnt)
            
        total = 0
        
        for i in range(1, len(group)):
            total += min(group[i], group[i-1])
            
        return total