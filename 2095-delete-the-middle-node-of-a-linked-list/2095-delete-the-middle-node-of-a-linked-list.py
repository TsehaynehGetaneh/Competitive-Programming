# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head.next
        
        
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            
            if not fast or not fast.next:
                slow.next = slow.next.next
            else:
                slow = slow.next
        
        return head
        