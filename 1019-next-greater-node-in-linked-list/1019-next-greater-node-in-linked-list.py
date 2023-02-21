# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        output = []
        stack = []
        i = 0
        
        curr = head
        while curr:
            value = curr.val
            if not stack or value <= stack[-1][1]:
                stack.append((i,value))
            else:
                while stack and stack[-1][1] < value:
                    idx = stack[-1][0]
                    output.append((idx,value))
                    stack.pop()
                stack.append((i,value))
                
            curr = curr.next
            i += 1
        print(stack)
        if stack:
            for i in range(len(stack)):
                output.append((stack[i][0],0))
                
        output_sort = sorted(output)
        print(output)
        res = []
        for i in range(len(output_sort)):
            res.append(output_sort[i][1])

        return res
            
            
        