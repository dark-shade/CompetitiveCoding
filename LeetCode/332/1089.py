"""1508 ms 14.7 MB
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """     
        j = len(arr) - 1
        
        for i in range(len(arr)):
            if j < i:
                j = len(arr) - 1
                continue
                
            if arr[i] == 0:                
                while j > i:
                    arr[j] = arr[j-1]
                    j -= 1
                    
        return
"""
"""64 ms
        arr_str = ''.join(map(str,arr))
        
        final_str = ""
        
        for s in arr_str.split('0'):
            final_str += s + "00"
            
        for i in range(len(arr)):
            arr[i] = int(final_str[i])
            
        return
"""