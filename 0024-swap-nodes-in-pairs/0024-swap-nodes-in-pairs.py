# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        if current == None:
            return None
        
        while current.next:
            current_val = current.val
            current.val = current.next.val
            current.next.val = current_val
            
            current = current.next.next
            
            if not current:
                break
        
        return head
        