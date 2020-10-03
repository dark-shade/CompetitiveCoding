class Solution:
    def confusingNumber(self, N: int) -> bool:
        if N == 0:
            return False
        
        inverted = ""
        original = N
        
        while N > 0:
            n = N % 10
            N = int(N/10)
            
            if n in [2,3,4,5,7]:
                return False
            else:
                if n in [0,1,8]:
                    inverted += str(n)
                elif n == 6:
                    inverted += "9"
                else:
                    inverted += "6"
        
        if int(inverted) != original:
            return True
        
        return False
            