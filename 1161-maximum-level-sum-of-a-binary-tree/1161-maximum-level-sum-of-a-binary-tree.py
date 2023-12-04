# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((1,root))
        dictry = defaultdict(int)
        dictry[1] = root.val
        
        while queue:
            level,current = queue.popleft()
            
            if current.left:
                dictry[level+1] += current.left.val
                queue.append((level+1, current.left))
                
            if current.right:
                dictry[level+1] += current.right.val
                queue.append((level+1,current.right))
        
        min_level = 1
        max_sum = float("-inf")
        for key in dictry:
            curr_sum = dictry[key]
            
            if curr_sum > max_sum:
                min_level = key
                max_sum = curr_sum
                
        return min_level
                
                
            
            
        