from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        fringe = [[root,0]]
        curr_level_val = 0
        running_level = 0
        running_cnt = 0
        final_list = []

        while fringe:
            curr_node, curr_level = fringe.pop(0)

            if curr_node.left:
                fringe.append([curr_node.left, curr_level + 1])
            
            if curr_node.right:
                fringe.append([curr_node.right, curr_level + 1])

            if curr_level != running_level:
                final_list.append(curr_level_val / running_cnt)
                curr_level_val = curr_node.val
                running_cnt = 1
                running_level = curr_level
            else:
                curr_level_val += curr_node.val
                running_cnt += 1
                
        final_list.append(curr_level_val / running_cnt)

        return final_list