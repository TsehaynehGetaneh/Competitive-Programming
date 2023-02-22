# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        if length == 0:
            return None
        if k >= length:
            k = k%length
        
        
            
        
        last = None
        newHead = head
        idx = 1
        while newHead:
            if length - k == idx:
                last = newHead.next
                newHead.next = None
                break
            
            newHead = newHead.next
            idx += 1
        if last == None:
            return head
        else:
            newCurr = last
            while newCurr and newCurr.next:
                newCurr = newCurr.next
            newCurr.next = head
            head = last
        
        print(head)
        return head
            
                    
        