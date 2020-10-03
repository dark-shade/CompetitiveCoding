""" 52 ms
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max_1 = -1
            max_1_ind = -1
            max_2 = -1
            max_2_ind = -1
            
            for i, w in enumerate(stones):
                if w > max_1:
                    max_2 = max_1
                    max_2_ind = max_1_ind
                    max_1 = w
                    max_1_ind = i            
                    continue
                elif w > max_2:
                    max_2 = w
                    max_2_ind = i
                    
            if max_1 == max_2:
                stones.remove(max_1)
                stones.remove(max_2)
                
            elif max_1 != max_2:
                stones[max_1_ind] = max_1 - max_2
                stones.remove(max_2)
                
        if len(stones) == 1:
            return stones[0]
        
        return 0
"""
""" 28 ms
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
                
            elif stones[0] != stones[1]:
                stones[1] = stones[0] - stones[1]
                stones.pop(0)
                
        if len(stones) == 1:
            return stones[0]
        
        return 0
"""
""" 32 ms
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
            
        heapq.heapify(stones)
        final_wt = 0
        
        while stones:
            w1 = heapq.heappop(stones)
            
            if not stones:
                final_wt = w1
                break
            
            w2 = heapq.heappop(stones)
            
            if w1 != w2:
                heapq.heappush(stones, w1 - w2)
                
        return final_wt * -1
"""
