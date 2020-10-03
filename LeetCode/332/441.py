class Solution:
    def arrangeCoins(self, n: int) -> int:
        root = math.sqrt(1 + 8*n)
        
        return max(int((-1 + root) / 2), int((-1 - root) / 2))
        