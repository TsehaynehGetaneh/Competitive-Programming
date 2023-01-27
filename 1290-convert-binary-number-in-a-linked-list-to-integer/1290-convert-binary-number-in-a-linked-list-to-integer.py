# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        bin_string = ""
        
        while head != None:
            bin_string += str(head.val)
            head = head.next
            
            
        return int(bin_string,2)
            