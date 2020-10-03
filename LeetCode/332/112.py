# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, target_sum: int) -> bool:
        if not root:
            return False
        
        fringe = [[root, [root.val]]]
        
        while fringe:
            cur, path = fringe.pop()
            
            if cur.right:
                fringe.append([cur.right, path + [cur.right.val]])
                
            if cur.left:
                fringe.append([cur.left, path + [cur.left.val]])
                
            if not cur.left and not cur.right:
                if target_sum == sum(path):
                    return True
                
            
        return False