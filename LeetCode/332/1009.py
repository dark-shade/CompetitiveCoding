"""48 ms
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = "{0:b}".format(N)
        f = ""
        for ch in binary:
            if ch == "1":
                f += "0"
            else:
                f += "1"
                
        return int(f,2)
"""
"""44 ms
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        ones = int("1" * len("{0:b}".format(N)), 2)
        
        return N ^ ones
"""