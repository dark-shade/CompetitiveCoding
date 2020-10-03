class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt_bull = 0
        cnt_cow = 0
        
        rem_g = ""
        rem_s = ""
        
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                cnt_bull += 1
            else:
                rem_s += secret[i]
                rem_g += guess[i]
            
        common = collections.Counter(rem_s) & collections.Counter(rem_g)
        
        for k in common:
            cnt_cow += common[k]
            
        f_str = ""
        f_str += str(cnt_bull) + "A"
        f_str += str(cnt_cow) + "B"
        
        return f_str