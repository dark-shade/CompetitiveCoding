# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        temp_root = root.left
        root.left = root.right
        root.right = temp_root

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root
"""

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        fringe = [root]

        while fringe:
            curr_node = fringe.pop()

            temp_node = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp_node

            if curr_node.left:
                fringe.append(curr_node.left)
            if curr_node.right:
                fringe.append(curr_node.right)
            
        return root
