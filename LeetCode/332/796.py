"""56 ms 13.8 MB
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) == 0 and len(B) == 0:
            return True
        for i in range(len(A)):
            if A[i+1:] + A[0:i+1] == B:
                return True
            
        return False
"""