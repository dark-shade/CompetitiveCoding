# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        # will contain [Node, depth]
        stack = [[root, 1]]
        max_depth = 0

        while stack:
            curr_node, depth = stack.pop()
            if curr_node.children != None:
                for child in curr_node.children:
                    stack.append([child, depth + 1])
            if depth > max_depth:
                max_depth = depth

        return max_depth


