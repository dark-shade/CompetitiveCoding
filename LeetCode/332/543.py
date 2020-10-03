"""56 ms 15.8 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # might be a better way, get sub-tree depth and add and keep track of max
        if not root:
            return 0
        
        _, d = self.getMaxPath(root)
        
        return d - 1
    
    # max_one_side_lenth, max_total_diameter
    def getMaxPath(self, node: TreeNode) -> (int, int):
        if not node:
            return 0, 0
        
        l = 0
        r = 0
        ml = 0
        mr = 0
        
        if node.right:
            r,mr = self.getMaxPath(node.right)
            
        if node.left:
            l,ml = self.getMaxPath(node.left)
            
        max_d = 0
        
        if r+l+1 > max(mr, ml):
            max_d = r+l+1
        else:
            max_d = max(mr, ml)
        
        return (max(r,l) + 1, max_d)
"""