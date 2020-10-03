""" 644 ms
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # of form {diff : [[num1, num2]]}
        diff = {}
        
        arr = sorted(arr)
        
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            
            if d not in diff:
                diff[d] = []
                
            diff[d].append([arr[i-1], arr[i]])
        
        return diff[min(diff)]
"""