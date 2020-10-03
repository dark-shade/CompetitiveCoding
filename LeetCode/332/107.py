""" 40 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # of form {level : [vals]}
        levels = {}
        
        fringe = [[root, 0]]
        
        while fringe:
            curr, level = fringe.pop(0)
            
            if level not in levels:
                levels[level] = []
                
            levels[level].append(curr.val)
            
            if curr.left:
                fringe.append([curr.left, level + 1])
                
            if curr.right:
                fringe.append([curr.right, level + 1])
                
        final_list = []
        
        for n in sorted(list(levels.keys()), reverse=True):
            final_list.append(levels[n])
            
        return final_list
"""
""" 32 ms
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        # of form {level : [vals]}
        levels = {}
        
        total_levels = 0
        
        fringe = [[root, 0]]
        
        while fringe:
            curr, level = fringe.pop(0)
            
            if level > total_levels:
                total_levels = level
            
            if level not in levels:
                levels[level] = []
                
            levels[level].append(curr.val)
            
            if curr.left:
                fringe.append([curr.left, level + 1])
                
            if curr.right:
                fringe.append([curr.right, level + 1])
                
        final_list = []
        
        for n in range(total_levels + 1):
            final_list.append(levels[total_levels - n])
            
        return final_list
"""
        