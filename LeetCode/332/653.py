# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        
        fringe = [root]
        visited = set()
        
        
        while fringe:
            curr = fringe.pop(0)
            visited.add(curr.val)
            
            if curr.left:
                fringe.append(curr.left)
                
            if curr.right:
                fringe.append(curr.right)
                
        for n in visited:
            if k - n in visited and k - n != n:
                return True
            
        return False