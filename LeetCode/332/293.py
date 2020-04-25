from typing import List

class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        final_list = set()

        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                if s[i] == "+":
                    if len(s) - 1 > i:
                        final_list.add(s[:i-1] + "--" + s[i+1:])
                    else:
                        final_list.add(s[:i-1] + "--")
        
        return list(final_list)
