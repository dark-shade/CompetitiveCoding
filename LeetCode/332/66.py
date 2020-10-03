class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        
        return [int(ch) for ch in str(int("".join(str(n) for n in digits)) + 1)]