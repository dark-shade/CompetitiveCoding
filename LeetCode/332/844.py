"""52 ms 13.7 MB
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s = []
        stack_t = []
        
        for ch in S:
            if ch == "#":
                if len(stack_s) > 0:
                    stack_s.pop()
            else:
                stack_s.append(ch)
                
        for ch in T:
            if ch == "#":
                if len(stack_t) > 0:
                    stack_t.pop()
            else:
                stack_t.append(ch)
                
        if stack_s == stack_t:
            return True
        
        return False    
"""
"""36 ms 13.8 MB
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        skip_ctr = 0
        t_new = ""
        s_new = ""
        
        for i in range(len(T)):
            if T[len(T) - 1 - i] == "#":
                skip_ctr += 1
            elif T[len(T) - 1 - i] != "#" and skip_ctr > 0:
                skip_ctr -= 1
            else:
                t_new += T[len(T) - 1 - i]
            
        skip_ctr = 0
        
        for i in range(len(S)):
            if S[len(S) - 1 - i] == "#":
                skip_ctr += 1
            elif S[len(S) - 1 - i] != "#" and skip_ctr > 0:
                skip_ctr -= 1
            else:
                s_new += S[len(S) - 1 - i]

        if t_new == s_new:
            return True
        
        return False
"""