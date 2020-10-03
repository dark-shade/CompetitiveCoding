# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return 0
        
        c_val = root.val
        
        fringe = [root]
        
        while fringe:
            curr = fringe.pop()
            
            if curr.val == target:
                c_val = curr.val
                break
                
            if abs(curr.val - target) < abs(c_val - target):
                c_val = curr.val
                
            if curr.val > target and curr.left:
                fringe.append(curr.left)
                
            if curr.val < target and curr.right:
                fringe.append(curr.right)

        return c_val
        