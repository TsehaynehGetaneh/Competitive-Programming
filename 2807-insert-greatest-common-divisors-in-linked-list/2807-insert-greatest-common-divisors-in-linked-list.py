# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            val1 = ptr.val
            val2 = ptr.next.val
            gcd = math.gcd(val1,val2)
            
            temp = ptr.next
            node = ListNode(gcd)
            ptr.next = node
            node.next = temp
            
            ptr = ptr.next.next
            
        return head