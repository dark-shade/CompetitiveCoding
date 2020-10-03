"""40 ms
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cnt = [0] * num_people
        curr = 1
        
        while candies > 0:
            for i in range(num_people):
                if candies - curr > 0:
                    cnt[i] += curr
                    candies -= curr
                    curr += 1                    
                else:
                    cnt[i] += candies
                    candies = 0
        
        return cnt
"""
