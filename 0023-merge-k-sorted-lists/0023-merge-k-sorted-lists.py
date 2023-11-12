# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for ll in lists:
            head = ll
            while head:
                vals.append(head.val)
                head = head.next
                
        vals.sort()
        if len(vals) == 0:
            return 
        
        head = ListNode(vals[0])
        curr = head
        
        for i in range(1,len(vals)):
            node = ListNode(vals[i])
            curr.next = node
            curr = curr.next
            
        return head
        