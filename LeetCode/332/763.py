"""64 ms 14 MB
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # get last indices of chars
        # of form {char : last_index}
        last = {}
        
        for i, ch in enumerate(S):
            if ch not in last:
                last[ch] = i
                continue
            last[ch] = i
        
        # get the partitions
        anchor = last[S[0]]
        cnt = 0
        part = []
        
        for i, ch in enumerate(S):
            cnt += 1
            
            if last[ch] > anchor:
                anchor = last[ch]
                
            if anchor == i:
                part.append(cnt)
                cnt = 0
        
        return part
"""