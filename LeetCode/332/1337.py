""" 208ms
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        wt = {}
        
        for i, r in enumerate(mat):
            cnt = r.count(1)
            
            if cnt not in wt:
                wt[cnt] = []
            wt[cnt].append(i)
            
        final_l = []
        
        for c in sorted(wt):
            final_l.extend(sorted(wt[c]))
            
        if k == len(mat):
            return final_l
        
        return final_l[:k]
"""
""" 136ms
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        wt = []
        
        for i in range(len(mat)):
            wt.append([i, mat[i].count(1)])
            
        wt = sorted(wt, key= operator.itemgetter(1))
        
        return [n for n, w in wt][:k]
"""
""" 120ms
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        wt = []
        
        for i in range(len(mat)):
            cnt = 0
            
            for j in mat[i]:
                if j == 0:
                    break
                cnt += 1
            
            wt.append([i, cnt])
            
        wt = sorted(wt, key= operator.itemgetter(1))
        
        return [n for n, w in wt][:k]
"""
