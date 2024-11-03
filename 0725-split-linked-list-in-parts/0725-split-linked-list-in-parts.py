# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        n, m = (l//k), (l%k)

        if n == 0:
            curr = head
            res = []
            while curr:
                res.append(ListNode(curr.val))
                curr = curr.next

            if len(res) < k:
                l = len(res)
                for i in range(l, k):
                    res.append(None)
            # print(res)
            return res

        else:
            res = []
            
            for i in range(k):
                curr = head
                idx = 0
                while idx < n and curr:
                    idx += 1
                    if idx < n:
                        curr = curr.next

                if m > 0:
                    curr = curr.next
                    m -=1

                res.append(head)
                if curr:
                    temp = curr.next
                    curr.next = None
                    head = temp

                # print(head, curr)

            
            return res

        
