"""36 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if (not root):
            return True
        
        if (not root.left and root.right) or (root.left and not root.right):
            return False
        
        l = self.traversal(root.left, "l")
        r = self.traversal(root.right, "r")
        
        print(l)
        print(r)
        
        if l == r:
            return True
        
        return False
        
        
    def traversal(self, root: TreeNode, direc: string) -> List[int]:
        fringe = [root]
        val = []
        
        while fringe:
            curr = fringe.pop(0)
            
            if curr:                
                val.append(curr.val)
            else:
                val.append(-1)
                continue
            
            if direc == "l":
                fringe.append(curr.left)
                fringe.append(curr.right)
                    
            if direc == "r":
                fringe.append(curr.right)
                fringe.append(curr.left)
            
        return val
"""