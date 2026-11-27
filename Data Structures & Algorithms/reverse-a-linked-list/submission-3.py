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
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt 
        return prev


# revrse linked list --> return head
# input can be empty


# negative and positive`
# prev = None 

# while curr 
    # next = curr.next (1)
    # curr.next = prev 0 --> None
    # prev = curr (0)
    # curr = next (1)
# return prev


