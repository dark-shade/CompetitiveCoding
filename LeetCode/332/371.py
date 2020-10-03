class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a >=0 and b >= 0:
            self.getSumBin(a, b)
            
        sign = 1 
        
        if (abs(a) >= abs(b) and a < 0) or (abs(b) >= abs(a) and b < 0):
            sign = -1
        
        if (a > 0 and b < 0) or (a < 0 and b > 0):
            return sign * (abs(a)^abs(b))
        
        return sign * self.getSumBin(abs(a), abs(b))
    
    def getSumBin(self, a:int, b:int) -> int:
        new_a = 1
        new_b = 1

        while new_a&new_b:
            new_a = ((a&b)<<1)
            new_b = (a^b)
            a = new_a
            b = new_b
        return ((a&b)<<1)|(a^b)
    
    def getSubBin(self, a:int, b:int) -> int:
        