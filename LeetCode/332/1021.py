"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        primitives = []
        final = ""
        prim = ""

        for ch in S:
            if len(stack) > 0 and ch == ")":
                if stack[-1] == "(":
                    stack.pop()
                    prim += ch                    
                    if len(stack) == 0:
                        primitives.append(prim)
                        prim = ""
            else:
                stack.append(ch)
                prim += ch
            
        
        for p in primitives:
            final += p[1:-1]

        return final
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []        
        final = ""
        prim = ""

        for ch in S:
            if len(stack) > 0 and ch == ")":
                if stack[-1] == "(":
                    stack.pop()
                    prim += ch                    
                    if len(stack) == 0:
                        final += prim[1:-1]
                        prim = ""
            else:
                stack.append(ch)
                prim += ch
            
        return final
