"""904 ms
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        
        monotone = ""
        
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                continue
            elif A[i] > A[i-1]:
                if len(monotone) == 0:
                    monotone = "inc"
                elif monotone != "inc":
                    return False
            else:
                if len(monotone) == 0:
                    monotone = "dec"
                elif monotone != "dec":
                    return False
                
        return True
"""
"""816 ms
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) == 1:
            return True
        
        monotone = 0
        
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                continue
            elif A[i] > A[i-1]:
                if monotone == 0:
                    monotone = 1
                elif monotone != 1:
                    return False
            else:
                if monotone == 0:
                    monotone = -1
                elif monotone != -1:
                    return False
                
        return True
"""