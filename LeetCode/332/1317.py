class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a, b = 1, n-1
        
        while self.hasZero(a) or self.hasZero(b):
            b -= 1
            a += 1
            
        return [a,b]
        
    def hasZero(self, num: int) -> bool:
        if "0" in str(num):
            return True
        
        return False