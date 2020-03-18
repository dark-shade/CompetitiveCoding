class Solution:
    def isArmstrong(self, N: int) -> bool:
        num = N
        sum = 0
        power = len(str(N))

        while N > 0:
            sum += pow(N%10, power)
            N = int(N/10)

        if sum == num:
            return True

        return False            


obj = Solution()
ams = obj.isArmstrong(123)
print(ams)