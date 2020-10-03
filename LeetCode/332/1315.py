"""108 ms 17.4 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        fringe = [[root, [root.val]]]
        sum_total = 0
        
        while fringe:
            cur, path = fringe.pop()
            
            if len(path) >= 3:
                if path[len(path)-3] % 2 == 0:
                    sum_total += cur.val
            
            if cur.left:
                fringe.append([cur.left, path + [cur.left.val]])
                
            if cur.right:
                fringe.append([cur.right, path + [cur.right.val]])
                
        return sum_total
"""