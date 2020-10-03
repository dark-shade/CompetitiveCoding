"""92 ms
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        max_sum = -1
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                s =  A[i] + A[j]
                if s < K:
                    if s > max_sum:
                        max_sum = s
                else:
                    break
                    
        return max_sum
"""
"""80 ms
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        max_sum = -1
        A.sort()
        
        for i in range(len(A)):
            j = len(A) - 1
            while j > i:
                s =  A[i] + A[j]
                if s < K:
                    if s > max_sum:
                        max_sum = s
                    break
                j -= 1
                    
        return max_sum
"""