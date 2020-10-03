class Solution:
    def isHappy(self, n: int) -> bool:
        n_set = set()
        n_set.add(n)
        curr = n
        
        while True:                
            curr = self.sumDigits(curr)
            if curr == 1:
                return True
            
            if curr in n_set:
                return False
            
            n_set.add(curr)
                
    def sumDigits(self, num):
        sum_digits = 0
        
        while num > 0:
            sum_digits += (num % 10)**2
            num = int(num/10)
            
        return sum_digits
        