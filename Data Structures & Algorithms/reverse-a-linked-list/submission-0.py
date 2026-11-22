# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            temp = curr.next  # save the next node to temp
            curr.next = prev  # flip the current pointer
            prev = curr  # the current node becomes the previous node of the next iteration
            curr = temp  # the next node to process
        
        return prev