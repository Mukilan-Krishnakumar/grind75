'''
Use a slow pointer and a fast pointer. Slow pointer moves by one 
fast pointer moves by two. If it is a cycle, they both will meet in O(n) time. 
If they meet return True, else False
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
