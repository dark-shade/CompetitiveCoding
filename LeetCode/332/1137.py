"""36 ms 13.7 MB
class Solution:
    def tribonacci(self, n: int) -> int:
        last_3 = [0,1,1]
        
        if n < 3:
            return last_3[n]
        
        for i in range(3, n):
            t3 = sum(last_3)
            last_3.pop(0)
            last_3.append(t3)
            
        return sum(last_3)
"""
