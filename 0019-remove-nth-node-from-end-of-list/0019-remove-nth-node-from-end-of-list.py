# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenOfList = 0
        currHead = head
        while currHead:
            lenOfList += 1
            currHead = currHead.next
            
        if lenOfList == 1:
            head = None
        elif lenOfList - n == 0:
            head = head.next
        else:
            curr = head
            idx = 1
            while curr:
                if lenOfList - n == idx:
                    temp = curr.next.next
                    curr.next = temp
                idx += 1
                curr = curr.next
        return head
        