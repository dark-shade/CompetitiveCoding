from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_cnt = self.coinChg(coins, amount)
        return min_cnt

    def coinChg(self, coins: List[int], amount: int) -> int:
        if coins == None or amount > 0:
            return -1
        
        if amount == 0:
            return 0
        
        curr_cnt = int(amount / coins[0])

        print("curr_cnt = ", curr_cnt)
        print("amount = ", amount)

        #return min(self.coinChg(coins, amount - curr_cnt * coins[pos], pos+1) + curr_cnt, self.coinChg(coins, amount, pos+1))
        return min(self.coinChg(coins.remove(coins[0]), amount - curr_cnt * coins[0]) + curr_cnt, self.coinChg(coins.remove(coins[0]), amount))


obj = Solution()
print(obj.coinChange([1,2,5], 11))