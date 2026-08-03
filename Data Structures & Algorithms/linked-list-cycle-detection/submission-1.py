# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

            if slow == fast:
                return True 
        
        return False


# fast and slow pointers
# if fast and slow ever equal --> then we knwo tehre is a cycle 

# first iteration = true
# slow = curr
# fast = curr.next

# while slow and fast
    # if slow == fast and not first ietati0n:
        # return true
    
    #fjkrst iteration =- false
    # slow = slow.next
    # fast = curr.next.next

# return false