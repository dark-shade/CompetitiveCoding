# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        unival = root.val
        fringe = [root]

        while fringe:
            curr = fringe.pop()

            if unival != curr.val:
                return False
            
            if curr.left:
                fringe.append(curr.left)
            if curr.right:
                fringe.append(curr.right)
        
        return True
        