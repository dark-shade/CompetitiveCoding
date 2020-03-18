from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        
        if not root:
            return order
        
        fringe = [root]
        
        while len(fringe) > 0:
            curr_node = fringe.pop()
            order.append(curr_node.val)

            ind = len(curr_node.children) - 1

            while ind > -1:
                fringe.append(curr_node.children[ind])
                ind -= 1

        return order
