# Lowest Common Ancestor of a Binary Search Tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root:TreeNode, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        maxValue = max(p.val,q.val)
        minValue = min(p.val,q.val)
        if(minValue > root.val):
            return self.lowestCommonAncestor(root.right,p,q)
        elif(maxValue< root.val):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root