class Solution:
    def generateTheString(self, n: int) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        final_str = ""

        if n % 2 == 0:
            final_str += alphabets[0]
            final_str += alphabets[1] * (n - 1)
        else:
            final_str += alphabets[0] * n

        return final_str
