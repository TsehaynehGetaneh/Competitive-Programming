# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = []
        current = head
        count = 1
        
        while current:
            temp.append((count, current.val))
            current = current.next 
            
        curr = head
        count2 = 1
        while curr:
            if count2 == k:
                curr.val = temp[len(temp) -k][1]
                
            if count2 == len(temp) -k +1:
                curr.val = temp[k-1][1]
                
            curr = curr.next
            count2 += 1
            
        return head
            
        