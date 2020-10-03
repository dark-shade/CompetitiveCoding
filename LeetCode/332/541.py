"""32ms 13.8 MB
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        cnt = len(s)//k 
        rev = True
        i = 0
        final_str = ""
        
        while i < cnt:
            if rev:
                final_str += s[i*k: i*k + k][::-1]
                rev = False
            else:
                final_str += s[i*k: i*k + k]
                rev = True
                
            i += 1
            
        if len(s) > cnt * k:
            if rev:                
                final_str += s[cnt*k:][::-1]
            else:
                final_str += s[cnt*k:]
                
        return final_str
"""