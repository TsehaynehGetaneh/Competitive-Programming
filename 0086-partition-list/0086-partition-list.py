# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        part1,part2 = ListNode(),ListNode()
        tail_part1 = part1
        tail_part2 = part2
        
        while head:
            if head.val < x:
                tail_part1.next = head
                tail_part1 = tail_part1.next
            else:
                tail_part2.next = head
                tail_part2 = tail_part2.next
                
            head = head.next
        
        tail_part2.next = None
        tail_part1.next = part2.next
        
        return part1.next
             
        