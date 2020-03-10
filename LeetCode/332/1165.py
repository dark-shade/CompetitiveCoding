class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        curr = 0
        cost = 0

        for ch in word:
            ind = keyboard.index(ch)
            cost += abs(curr - ind)
            curr = ind

        return cost

obj = Solution()
c = obj.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba")
print(c)
c = obj.calculateTime("pqrstuvwxyzabcdefghijklmno", "leetcode")
print(c)
