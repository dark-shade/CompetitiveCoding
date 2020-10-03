class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) == 0:
            return []
        
        cnt = 0
        prev = S[0]
        pos = []
        
        for i in range(len(S)):
            if prev == S[i]:
                cnt += 1
            else:
                if cnt >= 3:
                    pos.append([i-cnt,i-1])
                prev = S[i]
                cnt = 1
        
        if cnt >= 3:
            pos.append([i-cnt+1,i])
        
        return pos