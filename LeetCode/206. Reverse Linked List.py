class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous