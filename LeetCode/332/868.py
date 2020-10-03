class Solution:
    def binaryGap(self, N: int) -> int:
        max_gap = 0
        prev = -1
        
        for i, ch in enumerate(bin(N).split('b')[1]):
            if ch == "1":
                if prev == -1:
                    prev = i
                    continue
                
                if max_gap < i - prev:
                    max_gap = i - prev
                    
                prev = i
                
        return max_gap
                