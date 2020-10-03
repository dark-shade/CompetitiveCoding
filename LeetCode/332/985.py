""" TLE
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sols = []
        
        for q in queries:
            A[q[1]] += q[0]
            
            sum_even = 0
            
            for n in A:
                if n % 2 == 0:
                    sum_even += n
            
            sols.append(sum_even)
            
        return sols
"""
""" TLE
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sols = []
        
        even_indexes = []
        
        for i, n in enumerate(A):
            if n % 2 == 0:
                even_indexes.append(i)
        
        for q in queries:
            A[q[1]] += q[0]
            
            sum_even = 0
            
            if A[q[1]] % 2 != 0 and q[1] in even_indexes:
                even_indexes.remove(q[1])
            elif A[q[1]] % 2 == 0 and q[1] not in even_indexes:
                even_indexes.append(q[1])
            
            for n in even_indexes:
                sum_even += A[n]
            
            sols.append(sum_even)
            
        return sols
"""
""" 688 ms
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sols = []
        
        running_sum = 0
        
        for n in A:
            if n % 2 == 0:
                running_sum += n
        
        for q in queries:
            if A[q[1]] % 2 == 0:
                running_sum -= A[q[1]]
            
            A[q[1]] += q[0]
            
            if A[q[1]] % 2 == 0:
                running_sum += A[q[1]]
            
            sols.append(running_sum)
            
        return sols
"""
