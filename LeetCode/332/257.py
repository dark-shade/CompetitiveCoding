# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        fringe = [[root, str(root.val)]]
        leaf_paths = []
        
        
        while fringe:
            curr, path = fringe.pop()
            
            if curr.right:
                fringe.append([curr.right, path + "->" + str(curr.right.val)])
                
            if curr.left:
                fringe.append([curr.left, path + "->" + str(curr.left.val)])
                
            if not curr.right and not curr.left:
                leaf_paths.append(path)
        
        return leaf_paths