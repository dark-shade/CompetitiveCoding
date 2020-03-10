class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digitSum = 0
        digitProduct = 1

        while n > 0:
            digit = n % 10
            digitSum += digit
            digitProduct *= digit
            n = int(n/10)

        return digitProduct - digitSum

obj = Solution()
d = obj.subtractProductAndSum(100000)
print(d)
