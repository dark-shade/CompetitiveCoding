"""
class Solution:
    def freqAlphabets(self, s: str) -> str:
        next_two = 0
        next_chars = ""
        final_str = ""
        mapping = "abcdefghijklmnopqrstuvwxyz"

        for ch in s[::-1]:
            if ch == "#":
                next_two = 2
                continue

            if next_two > 0:
                next_chars += ch
                next_two -= 1
                if next_two > 0:
                    continue

            if len(next_chars) > 0:
                final_str += mapping[int(next_chars[::-1])-1]
                next_chars = ""
                continue

            final_str += mapping[int(ch)-1]
        
        return final_str[::-1]
"""

class Solution:
    def freqAlphabets(self, s: str) -> str:
        mapping = "abcdefghijklmnopqrstuvwxyz"

        for i in range(10,27):
            s = s.replace(str(i)+"#", mapping[i-1])
        
        for i in range(1, 11):
            s = s.replace(str(i), mapping[i - 1])
        
        return s
            

obj = Solution()
fstr = obj.freqAlphabets("1326#")
print(fstr)
