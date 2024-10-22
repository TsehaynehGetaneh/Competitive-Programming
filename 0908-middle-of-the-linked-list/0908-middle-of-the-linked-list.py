# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0

        curr = head
        while curr:
            curr = curr.next
            n += 1

        m = 0

        new_curr = head
        while new_curr:
            if m == n//2:
                return new_curr

            new_curr = new_curr.next
            m += 1