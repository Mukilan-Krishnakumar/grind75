# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Creating a dummy variable, so we don't hit the case of returning Non ListNode obj
        dummy = ListNode()
        # Pointer of sorts
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        # Whichever list is not null is appended in the end to the dummy
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
