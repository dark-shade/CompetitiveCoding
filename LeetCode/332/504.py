class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        
        base = ""
        n = abs(num)
        
        while n:
            base += str(n  % 7)
            n = n // 7
        
        if num < 0:
            return "-" + base[::-1]
        
        return base[::-1]
