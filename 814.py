# version 1 post-order traversal

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def pruneTree(self, root: TreeNode) -> TreeNode:
        
#         if root == None:
#             return None
        
#         root.left = self.pruneTree(root.left)
#         root.right = self.pruneTree(root.right)
        
#         if root.val == 0 and root.left == None and root.right == None:
#             return None
#         else:
#             return root

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        def contain_one(node: TreeNode) -> bool:
            if root is None:
                return False
            
            left_contain = contain_one(root.left) 
            right_contain = contain_one(root.right)

            if not left_contain:
                root.left = None
            
            if not right_contain:
                root.right = None

            
            return root.val == 1 or left_contain or right_contain


        if contain_one(root):
            return root
        else:
            return None           
        