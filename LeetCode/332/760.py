from typing import List

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        final = []

        for n in A:
            final.append(B.index(n))

        return final

obj = Solution()
f = obj.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
print(f)
