class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(set(arr))
        final_arr = []
        
        # of form {num : rank}
        rank = {}
        
        for i, n in enumerate(nums):
            rank[n] = i + 1
        
        for n in arr:
            final_arr.append(rank[n])
            
        return final_arr
    