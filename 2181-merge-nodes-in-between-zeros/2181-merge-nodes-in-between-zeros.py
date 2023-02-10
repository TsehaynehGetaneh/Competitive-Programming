# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head.next
        sub_sum = 0
        
        while right:
            if right.val == 0 and right.next == None:
                left.val = sub_sum
                left.next = None
                
            elif right.val == 0:
                left.val = sub_sum
                sub_sum = 0
                left.next = right
                left = left.next
                
            else:
                sub_sum += right.val
            
            right = right.next
        
        return head
        