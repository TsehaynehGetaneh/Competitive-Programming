# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hMap = {}
        while head:
            if head in hMap:
                return head
            hMap[head] = head.val
            head = head.next
        return None