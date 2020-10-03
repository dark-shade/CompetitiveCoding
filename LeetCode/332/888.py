"""TLE
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        B.sort()
        
        a_sum = sum(A)
        b_sum = sum(B)
        
        if a_sum < b_sum:
            return self.getSwap(A,B,a_sum,b_sum,"A")
        
        return self.getSwap(B,A,b_sum,a_sum,"B")
            
    def getSwap(self, smaller_list: List[int], larger_list: List[int], smaller_sum: int, larger_sum: int, smaller: string) -> List[int]:
        swap = []
        
        l_sum = larger_sum
        s_sum = smaller_sum
        
        for i in range(len(larger_list)):
            if larger_list[i] <= smaller_list[0]:
                continue
                
            for j in range(len(smaller_list)):
                if smaller_list[j] > larger_list[i]:
                    break
                    
                s_sum -= smaller_list[j]
                s_sum += larger_list[i]
                
                l_sum += smaller_list[j]
                l_sum -= larger_list[i]
                
                if s_sum == l_sum:
                    if smaller == "A":
                        swap.append(smaller_list[j])
                        swap.append(larger_list[i])
                    else:
                        swap.append(larger_list[i])
                        swap.append(smaller_list[j])
                        
                    return swap
                l_sum = larger_sum 
                s_sum = smaller_sum
            
            l_sum = larger_sum
            s_sum = smaller_sum
            
        return [0,0]
"""
