""" 220 ms 22.8 MB
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        score = 0
        total_cal = sum(calories[:k])
        trail_ctr = 0
        
        for i in range(k, len(calories)):
            if total_cal < lower:
                score -= 1
            elif total_cal > upper:
                score += 1
                
            total_cal -= calories[trail_ctr]
            trail_ctr += 1
            total_cal += calories[i]
                        
                
        if total_cal < lower:
            score -= 1
        elif total_cal > upper:
            score += 1
                
        return score
"""