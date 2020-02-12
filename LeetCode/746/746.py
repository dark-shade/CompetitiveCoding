from typing import List

class Solution:
    def __init__(self):
        self.mem = []

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for _ in range(len(cost)):
            self.mem.append(-1)

        cost = min(self.getCost(0, cost), self.getCost(1, cost))
        return cost

    def getCost(self, pos, cost):
        if pos >= len(cost):
            return 0

        if self.mem[pos] == -1:
            self.mem[pos] = min(self.getCost(pos+1, cost), self.getCost(pos+2, cost)) + cost[pos]
        
        return self.mem[pos]
    

obj = Solution()
print(obj.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))