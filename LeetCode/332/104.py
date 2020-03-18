# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        # of form [node, depth]
        fringe = [[root, 1]]
        max_depth = 0

        while len(fringe) > 0:
            curr_node, curr_depth = fringe.pop()

            if max_depth < curr_depth:
                max_depth = curr_depth

            if curr_node.right != None:
                fringe.append([curr_node.right, curr_depth + 1])

            if curr_node.left != None:
                fringe.append([curr_node.left, curr_depth + 1])

        return max_depth
