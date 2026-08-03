# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            next_val = curr.next 
            curr.next = prev # 0 --> 1
            prev = curr # 1
            curr = next_val # 2 

        return prev

# prev, curr, next
# if not head --> return []

# while curr:
    # next = curr.next 1
    # prev = curr 0 
    # curr = curr.next 1
    # curr.next = prev 1 --> 0
# return prev