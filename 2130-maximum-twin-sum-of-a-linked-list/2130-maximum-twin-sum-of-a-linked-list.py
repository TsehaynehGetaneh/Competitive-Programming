# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        max_sum = 1
        for i in range(len(arr)//2):
            sub_sum = arr[i] + arr[len(arr)-1-i]
            print(sub_sum)
            if sub_sum > max_sum:
                max_sum = sub_sum
                
                
                
        return max_sum