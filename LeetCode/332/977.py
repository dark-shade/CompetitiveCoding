from typing import List
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        final_list = []
        for n in A:
            final_list.append(n**2)
        
        final_list.sort()

        return final_list
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        final_list = []
        negative_ptr = 0
        positive_ptr = 0
        mid = 0

        for i, n in enumerate(A):
            if n >= 0:
                mid = i
                break
        
        positive_ptr = mid
        negative_ptr = mid - 1

        while len(final_list) != len(A):
            temp_neg = 0
            temp_pos = 0

            if negative_ptr >= 0:
                temp_neg = A[negative_ptr] ** 2
            
            if positive_ptr < len(A):
                temp_pos = A[positive_ptr] ** 2

            if temp_pos <= temp_neg:
                if positive_ptr < len(A):
                    final_list.append(temp_pos)
                    positive_ptr += 1
                else:
                    final_list.append(temp_neg)
                    negative_ptr -= 1

            elif temp_neg < temp_pos:
                if negative_ptr >= 0:
                    final_list.append(temp_neg)
                    negative_ptr -= 1
                else:
                    final_list.append(temp_pos)
                    positive_ptr += 1
            
        
        return final_list
                

obj = Solution()
l = obj.sortedSquares([-7,-3,2,3,11])
print(l)
