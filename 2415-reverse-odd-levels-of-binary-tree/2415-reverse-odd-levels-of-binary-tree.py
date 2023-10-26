# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rev(l, r, is_odd=True):
            if l is None or r is None:
                return
            if is_odd:
                l.val, r.val = r.val, l.val
            rev(l.left, r.right, not is_odd)
            rev(l.right, r.left, not is_odd)
        
        rev(root.left, root.right)

        return root
        