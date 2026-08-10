# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        len_linked_list = 0
        while curr:
            len_linked_list += 1
            curr = curr.next 
        
        rm_element_idx = len_linked_list - n
        rm_idx = rm_element_idx - 1

        curr_2 = head
        len_2 = 0
        while curr_2:
            if rm_element_idx == 0:
                return head.next
            if len_2 == rm_idx:
                curr_2.next = curr_2.next.next
                return head
            len_2 += 1
            curr_2 = curr_2.next




    
# lengt - n = index of element to be removed 

# iterate thrugh list 
    # one on the index of element to be removed - 1
    # set nodes next to the next next 
    # return 




