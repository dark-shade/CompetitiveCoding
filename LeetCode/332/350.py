class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ctr = collections.Counter(nums1)
        ctr &= collections.Counter(nums2)
        
        inter = []
        
        for n in ctr:
            inter.extend([n]*ctr[n])
            
        return inter