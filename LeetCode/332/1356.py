class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:        
        # form {bin.count("1"): []}
        wt = {}
        
        for n in arr:
            cnt = bin(n).count("1")
            
            if cnt not in wt:
                wt[cnt] = []
            wt[cnt].append(n)
                
        final_l = []
        
        for c in sorted(wt.keys()):
            final_l.extend(sorted(wt[c]))
            
        return final_l