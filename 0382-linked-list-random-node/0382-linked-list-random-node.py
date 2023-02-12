# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # total number of nodes
        slow = self.head
        i = 0
        while slow:
            i += 1
            slow = slow.next
        
        # import random number
        import random
        n = random.randint(0,i-1)
        print(n)
        
        # return value
        curr = self.head
        j = 0
        while curr:
            if j == n:
                return curr.val
            
            curr = curr.next
            j += 1
                

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()