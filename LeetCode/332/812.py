"""
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        
        for p1 in range(len(points)):
            for p2 in range(p1+1, len(points)):
                for p3 in range(p2+1, len(points)):
                    a = round(self.getDist(points[p1], points[p2]),6)
                    b = round(self.getDist(points[p2], points[p3]),6)
                    c = round(self.getDist(points[p3], points[p1]),6)
                    
                    s = (a + b + c)/2
                    
                    if s < a or s < b or s < c:
                        print("s = ", s)
                        print("a = ", a)
                        print("b = ", b)
                        print("c = ", c)

                    area = round((s*(s-a)*(s-b)*(s-c))**0.5,6)
                    
                    if area > max_area:
                        max_area = area
                        
        return max_area
                    
    def getDist(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5
"""
class Solution(object):
    def largestTriangleArea(self, points):
        def area(p, q, r):
            return .5 * abs(p[0]*q[1]+q[0]*r[1]+r[0]*p[1]
                           -p[1]*q[0]-q[1]*r[0]-r[1]*p[0])

        return max(area(*triangle)
            for triangle in itertools.combinations(points, 3))