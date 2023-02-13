# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        max_diff,min_diff = float("-inf"),float("inf")
        
        if not head.next.next:
            return [-1,-1]
        
        indices = []
        has_critical = False
        i = 0
        while head and head.next and head.next.next:
            prev = head.val
            curr = head.next.val
            nxt = head.next.next.val
            
            head = head.next
            
            i += 1
            if prev < curr > nxt or prev > curr < nxt:
                indices.append(i)
            
            if len(indices) > 1:
                has_critical = True
                max_diff = max(max_diff,indices[-1] - indices[0])
                min_diff = min(min_diff, indices[-1] - indices[-2])
                # print(indices[-1] - indices[-2])
        if not has_critical:
            return [-1,-1]

        return [min_diff,max_diff]
                
            
            
        
        