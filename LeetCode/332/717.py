"""56 ms 13.8 MB
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:        
        curr = ""
        last_zero = False
        
        for i in range(len(bits)):
            if len(curr) == 0:
                if bits[i] == 0:
                    last_zero = True
                    continue
                curr += str(bits[i])
                last_zero = False
                continue
                
            curr += str(bits[i])
            
            if curr == "11" or curr == "10":
                curr = ""
            else:
                print("there is something wrong")
                
        
        if len(curr) > 0:
            print("why is curr not empty")
        
        return last_zero
"""