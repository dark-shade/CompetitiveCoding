from typing import List

"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if points == None or len(points) == 0:
            return 0

        cnt = 0
        current_point = points[0]

        for point in points[1:]:
            while point != current_point:
                if current_point[0] < point[0]:
                    current_point[0] += 1
                elif current_point[0] > point[0]:
                    current_point[0] -= 1
                
                if current_point[1] < point[1]:
                    current_point[1] += 1
                elif current_point[1] > point[1]:
                    current_point[1] -= 1
                
                cnt += 1

        return cnt
"""

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        current_point = points[0]
        cnt = 0

        for point in points:
            cnt += max(abs(point[0] - current_point[0]), abs(point[1] - current_point[1]))
            current_point = point

        return cnt
