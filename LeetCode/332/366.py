""" 36 ms 13.8 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        left = []
        right =[]
        
        if root.left:
            left = self.findLeaves(root.left)
            
        if root.right:
            right = self.findLeaves(root.right)
        
        i = 0
        leaves = []
        
        while i < max(len(right), len(left)):            
            if i < len(right) and i < len(left):
                leaves.append(left[i] + right[i])
            elif i < len(right):
                leaves.append(right[i])
            elif i < len(left):
                leaves.append(left[i])
            i += 1
            
        leaves.append([root.val])
            
        return leaves
"""
""" 24 ms 14.1 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        left = []
        right =[]
        
        if root.left:
            left = self.findLeaves(root.left)
            
        if root.right:
            right = self.findLeaves(root.right)
        
        i = 0
        leaves = []
        len_left = len(left)
        len_right = len(right)
        
        while i < max(len_right, len_left):
            if i < len_right and i < len_left:
                leaves.append(left[i] + right[i])
            elif i < len_right:
                leaves.append(right[i])
            elif i < len_left:
                leaves.append(left[i])
            i += 1
            
        leaves.append([root.val])
            
        return leaves
"""