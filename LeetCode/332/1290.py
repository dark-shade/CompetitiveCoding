# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary_num = ""

        while head:
            binary_num += str(head.val
            head = head.next
        
        if len(binary_num) > 0:
            return int(binary_num, 2)
        
        return 0
