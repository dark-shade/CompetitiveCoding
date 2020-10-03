class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0]*3
        
        for bill in bills:
            if bill == 5:
                change[0] += 1
                continue
            elif bill == 10:
                if change[0] > 0:
                    change[0] -= 1
                    change[1] += 1
                else:
                    return False
            else:
                if change[0] * 5 + change[1] * 10 >= bill - 5:
                    change[2] += 1
                    
                    bill -= 5
                    
                    if change[1] > 0:
                        change[1] -= 1
                        bill -= 10
                        
                    if change[0] * 5 >= bill:
                        change[0] -= bill // 5
                        bill = 0
                        
                    if bill != 0:
                        return False
                    
                else:
                    return False
            
        return True