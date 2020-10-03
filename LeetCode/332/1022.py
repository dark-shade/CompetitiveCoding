# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        fringe = [[root, str(root.val)]]
        sum_of_leaves = 0
        
        while fringe:
            curr_node, path = fringe.pop()
            
            if not curr_node.left and not curr_node.right:
                sum_of_leaves += int(path, 2)
                continue
            
            if curr_node.right:
                fringe.append([curr_node.right, path + str(curr_node.right.val)])
                
            if curr_node.left:
                fringe.append([curr_node.left, path + str(curr_node.left.val)])
                
        return sum_of_leaves
                