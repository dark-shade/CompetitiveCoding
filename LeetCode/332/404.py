"""48 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        fringe = [[root, "r"]]
        
        sum_left_leaves = 0
        
        while fringe:
            curr, direc = fringe.pop()
            
            if curr.left:
                fringe.append([curr.left, "l"])
                
            if curr.right:
                fringe.append([curr.right, "r"])
                
            if not curr.left and not curr.right and direc == "l":
                sum_left_leaves += curr.val
                
        return sum_left_leaves
"""