""" 56 ms 13.8 MB
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = {}
        
        for i in range(len(costs)):
            diff[i] = abs(costs[i][0] - costs[i][1])
            
        
        can = [k for k, v in sorted(diff.items(), key=lambda item: item[1], reverse=True)]
        #print(can)
        cnt_a = 0
        cnt_b = 0
        total_sum = 0
        
        num = len(costs)/2
        
        for k in can:
            if (costs[k][0] < costs[k][1] and cnt_a < num) or cnt_b == num:
                cnt_a += 1
                total_sum += costs[k][0]
                #print("for record %d went to city A" % k)
            else:
                cnt_b += 1
                total_sum += costs[k][1]
                #print("for record %d went to city B" % k)
                
        return total_sum
"""
"""36 ms
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by a gain which company has 
        # by sending a person to city A and not to city B
        costs.sort(key = lambda x : x[0] - x[1])
        
        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total
"""