# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr = list1
        idx = 0
        while idx < a:
            if idx+1 == a:
                temp = curr.next
                
                while list2 and list2.next:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
                    
                curr.next = list2
                curr = curr.next
                
                while temp and temp.next:
                    if idx+1 > b:
                        curr.next = temp
                        temp = temp.next
                        curr = curr.next
                    else:
                        temp = temp.next
                        
                    idx += 1
                    
                curr.next = temp
                curr = curr.next
                break
            
            curr = curr.next
            idx += 1
            
        return list1
        