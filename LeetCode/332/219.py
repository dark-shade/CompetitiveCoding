class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #{num : last_index}
        num_dict = {}
        
        for i, n in enumerate(nums):
            if n not in num_dict:
                num_dict[n] = i
                continue
            else:
                if abs(num_dict[n] - i) <= k:
                    return True
                else:
                    num_dict[n] = i
                
        return False
        