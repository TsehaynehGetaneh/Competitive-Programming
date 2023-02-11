# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return head.next
        
        
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next
            
        j = 0
        cur = head
        while cur and cur.next:
            if j + 1 == i//2:
                cur.next = cur.next.next
                cur = cur.next
                break
            
            cur = cur.next
            j += 1
        
        return head
        