class Solution:
    def toHexspeak(self, num: str) -> str:
        print(str(hex(int(num))).split('x')[1])
        
        final_hex = ""
        
        for ch in str(hex(int(num))).upper().split('X')[1]:
            if ch in ['2','3','4','5','6','7','8','9']:
                return "ERROR"
            
            if ch == "0":
                final_hex += "O"
                
            elif  ch == "1":
                final_hex += "I"
            
            else:
                final_hex += ch
                
        return final_hex
                