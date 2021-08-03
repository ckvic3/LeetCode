# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = 0

        def help(node:TreeNode):
            if(node == None):
                return None
            leftVal = help(node.left)
            
            if(self.k == k):
                return leftVal
            elif self.k == k -1:
                self.k = k
                return root.val
            else:
                self.k = self.K + 1
                 
            rightval = help(node.right)
            return rightval
        
        return help(root)
        