class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_a = 0
        cnt_l = 0
        
        for ch in s:
            if ch == "A":
                cnt_a += 1
                
                if cnt_a > 1:
                    return False
                
            if ch == "L":
                cnt_l += 1
                
                if cnt_l > 2:
                    return False
            else:
                cnt_l = 0
                
        return True
            