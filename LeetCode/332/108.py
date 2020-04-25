from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        mid = int(len(nums) / 2)

        curr_node = TreeNode(nums[mid])

        if len(nums) >= mid:
            curr_node.left = self.sortedArrayToBST(nums[:mid])

        if len(nums) >= mid+1:
            curr_node.right = self.sortedArrayToBST(nums[mid+1:])

        return curr_node
