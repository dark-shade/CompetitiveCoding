from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

"""
# this is also an accepted solution
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []
                
        if not root:
            return order
        
        fringe = [root]
        already_visited = []

        while len(fringe) > 0:
            curr_node = fringe.pop()
            childs = []

            if curr_node.children != None and len(curr_node.children) > 0:
                ind = len(curr_node.children) - 1
                
                while ind > -1:
                    if curr_node.children[ind] not in already_visited:
                        childs.append(curr_node.children[ind])
                    ind -= 1
                    
            if len(childs) > 0:
                fringe.append(curr_node)
                fringe.extend(childs)
            else:
                order.append(curr_node.val)
                already_visited.append(curr_node)
        
        return order
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []

        if not root:
            return order

        fringe = [root]

        while fringe:
            curr_node = fringe.pop()
            order.append(curr_node.val)

            if curr_node.children:
                fringe.extend(curr_node.children)

        return order[::-1]
                