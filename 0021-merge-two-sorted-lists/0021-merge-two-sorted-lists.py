# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head = None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val <= list2.val:
                self.head = list1
                list1 = list1.next
                
                head = self.head
                curr = head
                while list1 and list2:
                    if list1.val <= list2.val:
                        curr.next = list1
                        curr = curr.next
                        list1 = list1.next
                    else:
                        curr.next = list2
                        curr = curr.next
                        list2 = list2.next
                
                while list1:
                    curr.next = list1
                    curr = curr.next
                    list1 = list1.next
                    
                while list2:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
                    
            else:
                self.head = list2
                list2 = list2.next

                head = self.head
                curr = head
                while list1 and list2:
                    if list1.val <= list2.val:
                        curr.next = list1
                        curr = curr.next
                        list1 = list1.next
                    else:
                        curr.next = list2
                        curr = curr.next
                        list2 = list2.next

                while list1:
                    curr.next = list1
                    curr = curr.next 
                    list1 = list1.next

                while list2:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
                
            return head
                    
                    
            
                        
                        
            
            