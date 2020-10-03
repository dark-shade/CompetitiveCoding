""" 84 ms 14 MB
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()

        min_abs = 0
        
        for i in range(len(A)):
            if abs(A[min_abs]) > abs(A[i]):
                min_abs = i
                
            if A[i] < 0:
                A[i] *= -1
                K -= 1
                
                if K == 0:
                    break
                
            else:
                if K > 0:
                    A[min_abs] *= math.pow(-1,K)
                break
                
        return int(sum(A))
"""
""" 53 ms 13.8 MB
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        heapq.heapify(A)
        
        while K > 0:
            heapq.heappush(A,-heapq.heappop(A))
            K -= 1
            
        return sum(list(A))
"""