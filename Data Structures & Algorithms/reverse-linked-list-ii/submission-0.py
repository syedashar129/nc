# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # edge case 
        if left == right:
            return head

        # setup
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next

        # 1: Reverse
        prev_rev = None 
        curr_rev = curr 

        for _ in range(right - left + 1): # reverse window
            nxt = curr_rev.next 
            curr_rev.next = prev_rev 
            prev_rev = curr_rev
            curr_rev = nxt
        
        # 2: Stitch 
        prev.next = prev_rev
        curr.next = curr_rev

        return dummy.next




# head, left, right 
# left <= right
# 1-indexed 
# end goal: left --> right 

# reverse partial (left --> right)