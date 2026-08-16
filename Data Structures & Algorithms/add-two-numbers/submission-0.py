# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # setup 
        dummy = ListNode()
        curr = dummy 
        carry = 0 

        while l1 or l2 or carry:
            # 1: Get values (use 0 if empty)
            val1 = l1.val if l1 else 0 
            val2 = l2.val if l2 else 0 

            # 2: Do math 
            total = val1 + val2 + carry
            carry = total // 10
            val = total % 10

            # 3: create new node and attach it
            curr.next = ListNode(val)

            # 4: move all pointers forward
            curr = curr.next 
            if l1: 
                l1 = l1.next 
            if l2:
                l2 = l2.next

        return dummy.next

        
        

# positive numbers
# revre order 
# all single digit
# 2 linked list s
# add both together by order and return them in order


