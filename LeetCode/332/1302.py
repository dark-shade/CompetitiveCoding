""" 104 ms and 17.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_depth = 0
        max_depth_sum = 0
        fringe = [[root, 0]]
        
        while fringe:
            cur, depth = fringe.pop()
            
            if depth > max_depth:
                max_depth = depth
                max_depth_sum = cur.val
            elif depth == max_depth:
                max_depth_sum += cur.val
                
            if cur.left:
                fringe.append([cur.left, depth+1])
                
            if cur.right:
                fringe.append([cur.right, depth+1])
                
        return max_depth_sum
"""
""" 88 ms and 17.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        max_depth_sum = 0
        
        fringe = [root]
        current = []
        
        while fringe:
            current = fringe
            fringe = []
            
            for node in current:
                if node.left:
                    fringe.append(node.left)
                if node.right:
                    fringe.append(node.right)
                    
        for node in current:
            max_depth_sum += node.val
            
        return max_depth_sum
"""