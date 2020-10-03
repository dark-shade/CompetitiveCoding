class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if len(arr) < 3:
            return arr
                
        changes = True
        
        while changes:
            changes = False

            new_arr = list(arr)
            
            for i in range(1, len(arr) - 1):            
                if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    new_arr[i] -= 1
                    changes = True
                elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    new_arr[i] += 1
                    changes = True
                    
            arr = new_arr
        
        return arr
                

    