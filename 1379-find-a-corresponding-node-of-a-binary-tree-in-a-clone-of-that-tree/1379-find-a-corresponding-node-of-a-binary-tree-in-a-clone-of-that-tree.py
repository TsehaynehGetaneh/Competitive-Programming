# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        node = None
    
    
        def helper(original,cloned,tar):
            nonlocal node
            if not cloned:
                return

            if cloned.val == target.val:
                node = cloned
                print("hey")
                return
            else:
                print("hey2")
                helper(original,cloned.left,tar)
                helper(original,cloned.right,tar)
                
            return node
        helper(original,cloned,target)
        return node
        
        
        