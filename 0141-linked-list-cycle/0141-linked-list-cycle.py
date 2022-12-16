# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hMap = {}
        current = head
        while current:
            if current in hMap:
                return True
            hMap[current] = 1
            current = current.next
        return False
        