"""484 ms
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        target_sum = int(sum(A)/3)
        
        curr_sum = 0
        cnt = 0
        
        for n in A:
            curr_sum += n
            
            if curr_sum == target_sum:
                cnt += 1
                curr_sum = 0
        
        if cnt >= 3:
            return True
        
        return False
"""
"""420 ms
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total_sum = sum(A)
        
        if total_sum % 3 != 0:
            return False
        
        target_sum = int(total_sum/3)
        
        curr_sum = 0
        cnt = 0
        
        for n in A:
            curr_sum += n
            
            if curr_sum == target_sum:
                cnt += 1
                curr_sum = 0
        
        if cnt >= 3:
            return True
        
        return False
"""
"""396 ms
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total_sum = sum(A)
        
        if total_sum % 3 != 0:
            return False
        
        target_sum = int(total_sum/3)
        
        curr_sum = 0
        cnt = 0
        
        for n in A:
            curr_sum += n
            
            if curr_sum == target_sum:
                cnt += 1
                curr_sum = 0
                
                if cnt == 3:
                    return True
        
        return False
"""
"""424 ms
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total_sum = sum(A)
        
        if total_sum % 3 != 0:
            return False
        
        target_sum = total_sum//3
        
        curr_sum = 0
        cnt = 0
        
        for i in range(len(A)):
            curr_sum += A[i]
            
            if curr_sum == target_sum:
                cnt += 1
                curr_sum = 0
                
                if cnt == 2:
                    break
        
        return cnt == 2 and i < len(A) - 1
"""
