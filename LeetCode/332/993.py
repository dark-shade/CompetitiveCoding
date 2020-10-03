"""36 ms 14 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
            if not root:
                return False
            
            fringe = [[root, 0, root.val]]
            x_d = 0
            x_p = 0
            y_d = 0
            y_p = 0
            
            while fringe:
                cur, depth, parent = fringe.pop()
                
                if x == cur.val:
                    x_d = depth
                    x_p = parent
                    
                if y == cur.val:
                    y_d = depth
                    y_p = parent
                    
                
                if y_d != 0 and x_d != 0:
                    if x_d == y_d and y_p != x_p:
                        return True
                    return False        
                
                if cur.left:
                    fringe.append([cur.left, depth+1, cur.val])
                    
                if cur.right:
                    fringe.append([cur.right, depth+1, cur.val])
"""
"""28 ms 13.7 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
            if not root:
                return False
            
            fringe = [[root, 0, root.val]]
            x_d = 0
            x_p = 0
            y_d = 0
            y_p = 0
            
            while fringe:
                cur, depth, parent = fringe.pop()
                
                if x == cur.val:
                    x_d = depth
                    x_p = parent
                    if y_d != 0 and x_d != 0:
                        if x_d == y_d and y_p != x_p:
                            return True
                        return False  
                    continue
                    
                if y == cur.val:
                    y_d = depth
                    y_p = parent
                    if y_d != 0 and x_d != 0:
                        if x_d == y_d and y_p != x_p:
                            return True
                        return False  
                    continue
                      
                
                if cur.left:
                    fringe.append([cur.left, depth+1, cur.val])
                    
                if cur.right:
                    fringe.append([cur.right, depth+1, cur.val])
"""