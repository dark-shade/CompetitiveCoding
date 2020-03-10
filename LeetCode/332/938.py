# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root == None:
            return 0
        
        sumTotal = 0

        if root.left:
            sumTotal += self.rangeSumBST(root.left, L, R)
        if root.right:
            sumTotal += self.rangeSumBST(root.right, L, R)

        if root.val >= L and root.val <= R:
            sumTotal += root.val
        
        return sumTotal

