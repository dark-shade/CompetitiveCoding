class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        if len(S) == 0:
            return ""
        
        reversed_S = ""
        
        for i in range(len(S)):
            if (ord(S[len(S) - 1 - i]) >= 65 and ord(S[len(S) - 1 - i]) <= 90) or (ord(S[len(S) - 1 - i]) >= 97 and ord(S[len(S) - 1 - i]) <= 122):
                reversed_S += S[len(S) - 1 - i]
        
        reverse_ptr = 0
        f_str = ""
        
        for i in range(len(S)):
            if (ord(S[i]) >= 65 and ord(S[i]) <= 90) or (ord(S[i]) >= 97 and ord(S[i]) <= 122):
                f_str += reversed_S[reverse_ptr]
                reverse_ptr += 1
            else:
                f_str += S[i]
                
        return f_str
                