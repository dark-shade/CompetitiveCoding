"""76 ms 14.9 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        min_depth = float('inf')
        fringe = [[root, [root.val]]]
        
        while fringe:
            cur, path = fringe.pop()
            
            if not cur.left and not cur.right:
                if len(path) < min_depth:
                    min_depth = len(path)
                    
            if len(path) > min_depth:
                continue
                    
            if cur.left:
                fringe.append([cur.left, path + [cur.left.val]])
                
            if cur.right:
                fringe.append([cur.right, path + [cur.right.val]])
                
        return min_depth
"""
"""36 ms 15 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 1
        fringe = [root]
        
        while fringe:
            current = fringe
            fringe = []
            
            for cur in current:
                if not cur.left and not cur.right:
                    return depth

                if cur.left:
                    fringe.append(cur.left)

                if cur.right:
                    fringe.append(cur.right)

            if len(fringe) > 0:
                depth += 1
"""