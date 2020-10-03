# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        cnt = self.calcSubTree(root)
        
        if cnt == -1:
            return False
        
        return True
        
    def calcSubTree(self, node: TreeNode) -> int:
        left = 0
        right = 0
        cnt = 0
        
        if node.left:
            left = self.calcSubTree(node.left)
            if left == -1:
                return -1
            
        if node.right:
            right = self.calcSubTree(node.right)
            if right == -1:
                return -1
            
        if abs(right - left) > 1:
            return -1
               
        return max([left, right]) + 1