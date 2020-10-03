"""56 ms 17.9 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        fringe = [root]
        ctr = {}
        
        while fringe:
            cur = fringe.pop()
            
            if cur.val not in ctr:
                ctr[cur.val] = 0
            
            ctr[cur.val] += 1
            
            if cur.right:
                fringe.append(cur.right)
                
            if cur.left:
                fringe.append(cur.left)
                
        max_value = max(ctr.values())
        modes = []
        
        for k in ctr:
            if max_value == ctr[k]:
                modes.append(k)
                
        return modes
"""
