"""664 ms
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        ranks = []
    
        scores_sorted = sorted(nums, reverse=True)
        
        for n in nums:
            rank = scores_sorted.index(n)
            
            if rank > 2:
                ranks.append(str(rank + 1))
            elif rank == 2:
                ranks.append("Bronze Medal")
            elif rank == 1:
                ranks.append("Silver Medal")
            else:
                ranks.append("Gold Medal")
                
        return ranks        
"""