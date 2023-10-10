# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_nodes = []
        if head == None:
            return False
        while head.next != None:
            if head in visited_nodes:
                return True
            visited_nodes.append(head)
            head = head.next
        return False
