# Flatten Binary Tree to Linked List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = TreeNode()
        self._flatten(root)
    
    def _flatten(self,root: TreeNode):
        if root is not None:
            self.prev.right = root
            self.prev = root
            rightChild = root.right
            self._flatten(root.left)
            root.left = None
            self._flatten(rightChild)
    


        