# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        
        fringe = [[root, None]]
        head = None

        while fringe:
            curr_node, parent = fringe.pop()

            if not head:
                if curr_node.val >= L and curr_node.val <= R:
                    head = curr_node
                elif curr_node.val < L and curr_node.right:
                    fringe.append([curr_node.right, None])
                    continue
                elif curr_node.val > R and curr_node.left:
                    fringe.append([curr_node.left, None])
                    continue
            
            if not head:
                break

            if curr_node.val >= L and curr_node.val <= R:
                if curr_node.right:
                    fringe.append([curr_node.right, curr_node])

                if curr_node.left:
                    fringe.append([curr_node.left, curr_node])
                
            elif curr_node.val < L:
                if curr_node.right:
                    parent.left = curr_node.right
                    fringe.append([curr_node.right, parent])
                else:
                    parent.left = None
            
            elif curr_node.val > R:
                if curr_node.left:
                    parent.right = curr_node.left
                    fringe.append([curr_node.left, parent])
                else:
                    parent.right = None

        return head

