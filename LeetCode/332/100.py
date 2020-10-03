# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # performing in-order traversal
        # traversal for p
        p_inord = self.inorditr(p)
            
            
        # traversal for q
        q_inord = self.inorditr(q)
        
        print(p_inord)
        print(q_inord)
        
        if len(p_inord) == len(q_inord):
            for i in range(len(p_inord)):
                if p_inord[i] != q_inord[i]:
                    return False
            return True
        
        return False
    
    def inorderrec(self, node):
        if not node:
            return []
        
        inord = []

        if node.left:
            inord = self.inorderrec(node.left)
        elif node.right:
            inord.append("None")
            
        inord.append(node.val)

        if node.right:
            inord.extend(self.inorderrec(node.right))
        elif node.left:
            inord.append("None")

        return inord
        
    def inorditr(self, node):
        if not node:
            return []
        
        inord = []
        fringe = [node]

        while fringe:
            curr_node = fringe.pop()

            if curr_node.right and curr_node.right not in fringe:
                fringe.append(curr_node.right)
            elif not curr_node.left:
                inord.append("None")

            if curr_node.left and curr_node.left not in inord:
                fringe.append(curr_node)
                fringe.append(curr_node.left)
                if not curr_node.right:
                    inord.append("None")
                continue
            
            inord.append(curr_node)

        inord_val = []

        for node in inord:
            if node == "None":
                inord_val.append(node)
            else:    
                inord_val.append(node.val)

        return inord_val       



        