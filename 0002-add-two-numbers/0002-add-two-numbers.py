# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1,curr2 = l1,l2
        
        if not curr1:
            return curr1
        if not curr2:
            return curr2
        
        stack = [0]
        newHead = None
        curr = newHead
        while curr1 and curr2:
            if not newHead:
                value = curr1.val + curr2.val + stack[0]
                if value < 10:
                    newHead =ListNode(value)
                    curr = newHead 
                else:
                    v = str(value)
                    newHead = ListNode(int(v[1]))
                    curr = newHead
                    stack[0] = int(v[0])
            else:
                value =  curr1.val + curr2.val + stack[0]
                if value > 9:
                    v = str(value)
                    curr.next = ListNode(int(v[1]))
                    curr = curr.next
                    stack[0] = int(v[0])
                else:
                    curr.next = ListNode(value)
                    curr = curr.next
                    stack[0] = 0
                
            curr1 = curr1.next
            curr2 = curr2.next
            
        if curr1:
            while curr1:
                value = curr1.val + stack[0]
                if value > 9:
                    v = str(value)
                    curr.next = ListNode(int(v[1]))
                    curr = curr.next
                    stack[0] = int(v[0])
                else:
                    curr.next = ListNode(value)
                    curr = curr.next
                    stack[0] = 0
                
                curr1 = curr1.next
        if curr2:
            while curr2:
                value = curr2.val + stack[0]
                if value > 9:
                    v = str(value)
                    curr.next = ListNode(int(v[1]))
                    curr = curr.next
                    stack[0] = int(v[0])
                else:
                    curr.next = ListNode(value)
                    curr = curr.next
                    stack[0] = 0
                
                curr2 = curr2.next
                
        if stack[0] > 0:
            curr.next = ListNode(stack[0])
            curr = curr.next
                
        return newHead
        