class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        power = len(s) - 1

        for ch in s:
            num += pow(26, power) * (ord(ch) - 64)
            power -= 1

        return num
