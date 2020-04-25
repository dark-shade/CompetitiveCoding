# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        fringe = [root]
        visited = []
        curr_node = None

        while fringe:
            curr_node = fringe.pop()
            visit = True

            if curr_node.left and curr_node.left not in fringe and curr_node.left not in visited:
                fringe.append(curr_node.left)
                fringe.append(curr_node)
                visit = False

            if curr_node.right and curr_node.right not in fringe and curr_node.right not in visited:
                if curr_node not in fringe:
                    fringe.append(curr_node)
                fringe.append(curr_node.right)
                visit = False

            if visit:
                prev_node = None
                if len(visited) > 0:
                    prev_node = visited[-1]
                curr_node.right = prev_node
                curr_node.left = None
                visited.append(curr_node)
        
        return curr_node
