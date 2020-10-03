""" 36 ms
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even_cnt = 0
        odd_cnt = 0
        
        for n in chips:
            if n % 2 == 0:
                even_cnt += 1
            else:
                odd_cnt += 1
                
        if even_cnt > odd_cnt:
            return odd_cnt
        
        return even_cnt
"""
""" 32 ms
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        counter = collections.Counter(chips)
        
        odd_cnt = 0
        even_cnt = 0
        
        for k in counter:
            if k % 2 == 0:
                even_cnt += counter[k]
            else:
                odd_cnt += counter[k]
        
        return min(odd_cnt, even_cnt)
"""
