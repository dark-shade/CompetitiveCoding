"""48 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        fringe = [root]
        
        values = []
        
        while fringe:
            curr = fringe.pop()
            
            values.append(curr.val)
            
            if curr.right:
                fringe.append(curr.right)
                
            if curr.left:
                fringe.append(curr.left)
                
        values.sort()
        
        min_diff = -1
              
        for i in range(1, len(values)):
            if values[i] - values[i-1] < min_diff or min_diff == -1:
                min_diff = values[i] - values[i-1]
                
        return min_diff
"""