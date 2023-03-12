# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        result = self.inorder(root)
        
        new_tree = TreeNode(result[0])
        tree = new_tree
        
        for i in range(1,len(result)):
            node = TreeNode(result[i])
            
            new_tree.right = node
            new_tree = new_tree.right
                
        return tree
        
        
    def inorder(self,node):
        if not node:
            return []
        
        curr = [node.val]
        left = self.inorder(node.left)
        right = self.inorder(node.right)
        
        return left + curr + right