class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None and head.next is not None:
            prev = None
            cur = head
            nex = head.next
            while nex is not None:
                if cur.val == nex.val:
                    while nex is not None and nex.val == cur.val:
                        nex = nex.next
                    if prev is None:
                        head = nex
                    else:
                        prev.next = nex
                else:
                    prev = cur
                cur = nex
                if nex is not None:
                    nex = nex.next
        return head