from typing import List

"""
# brute force, TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.getProfit(prices, 0)

    def getProfit(self, prices, day):
        if day >= len(prices):
            return 0

        profit = 0
        
        for i in range(day, len(prices)):
            max_profit = 0

            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    curr_profit = prices[j] - prices[i] + self.getProfit(prices, j + 1)

                    if curr_profit > max_profit:
                        max_profit = curr_profit

            if max_profit > profit:
                profit = max_profit

        return profit
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for day in range(1, len(prices)):
            if prices[day] > prices[day - 1]:
                profit += prices[day] - prices[day - 1]

        return profit
            