""" 544 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        fringe = [root]
        visited = []
        running_sum = 0
        
        while fringe:
            curr_node = fringe.pop()
            
            if (not curr_node.left or curr_node.left in fringe) and (not curr_node.right or curr_node.right in visited):
                curr_node.val += running_sum
                running_sum = curr_node.val
                visited.append(curr_node)
                continue
            
            if curr_node.left:
                fringe.append(curr_node.left)
                
            fringe.append(curr_node)
            
            if curr_node.right:
                fringe.append(curr_node.right)
                
        return root
"""
[10,8,12,7,9,11,13]