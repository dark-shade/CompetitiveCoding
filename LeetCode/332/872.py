# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leafs_root_1 = []
        leafs_root_2 = []

        fringe = [root1]

        while fringe:
            curr_node = fringe.pop()

            if not curr_node.left and not curr_node.right:
                leafs_root_1.append(curr_node.val)
            if curr_node.right:
                fringe.append(curr_node.right)
            if curr_node.left:
                fringe.append(curr_node.left)
            
            
        fringe = [root2]

        while fringe:
            curr_node = fringe.pop()

            if not curr_node.left and not curr_node.right:
                leafs_root_2.append(curr_node.val)
            if curr_node.right:
                fringe.append(curr_node.right)
            if curr_node.left:
                fringe.append(curr_node.left)
                            
        if len(leafs_root_1) != len(leafs_root_2):
            return False

        for i in range(len(leafs_root_1)):
            if leafs_root_1[i] != leafs_root_2[i]:
                return False
        
        return True
        