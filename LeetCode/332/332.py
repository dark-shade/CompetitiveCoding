from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        if len(coins) == 0:
            print("here1")
            return -1
        
        num = self.coinChg(coins, amount)

        if num >= 999999:
            print("here2")
            return -1

        return num

    def coinChg(self, coins: List[int], amount: int) -> int:
        if coins != None or len(coins) == 0:
            if amount == 0:
                return 0
            else:
                return 999999
        
        if amount % coins[0] != 0:
            return 0

        return min(self.coinChange(coins.remove(coins[0]), amount), self.coinChange(coins.remove(coins[0]), amount%coins[0]) + int(amount/coins[0]))

obj = Solution()
print(obj.coinChange([1,2,5], 11))