"""68 ms 15.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        l = (0,0)
        r = (0,0)
        
        if root.left:
            l = self.calcTilt(root.left)
            
        if root.right:
            r = self.calcTilt(root.right)
            
        return abs(l[1]-r[1]) + l[0] + r[0]

        
    # returns (tilt of node, sum of children self)
    def calcTilt(self, node:TreeNode) -> (int, int):
        if not node:
            return (0,0)
        
        l = (0,0)
        r = (0,0)
        
        if node.left:
            l = self.calcTilt(node.left)
            
        if node.right:
            r = self.calcTilt(node.right)
            
        return (abs(l[1]-r[1]) + l[0] + r[0], l[1] + r[1] + node.val)
"""
