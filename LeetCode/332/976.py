"""244 ms
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        
        peri = 0
        
        for i in range(2,len(A)):
            if A[i] < A[i-1] + A[i-2]:
                peri = A[i] + A[i-1] + A[i-2]
                
        return peri
"""
"""208 ms
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        
        peri = 0
        
        for i in range(2,len(A)):
            if A[i-2] < A[i-1] + A[i]:
                peri = A[i] + A[i-1] + A[i-2]
                break
                
        return peri
"""