# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left,right = ListNode(),ListNode()
        tLeft,tRight = left,right
        idx = 1
        
        while head:
            if idx%2 != 0:
                tLeft.next = head
                tLeft = tLeft.next
            else:
                tRight.next = head
                tRight = tRight.next
                
            head = head.next
            idx += 1
        
        tLeft.next = right.next
        tRight.next = None
        
        
        return left.next