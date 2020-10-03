class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1) - 1
        l2 = len(num2) - 1
        carry = ""
        s = ""
        
        while l1 >= 0 or l2 >= 0:
            total = 0
            
            if l1 >= 0:
                total += int(num1[l1])
                l1 -= 1
                
            if l2 >= 0:
                total += int(num2[l2])
                l2 -= 1
                
            if len(carry) > 0:
                total += int(carry)
                carry = ""
            
            ts = str(total)
            
            if len(ts) > 1:
                carry = ts[:-1]
            
            s = ts[-1] + s
            
            
        s = carry + s
        
        return s
            