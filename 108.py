# Convert Sorted Array to Binary Search Tree
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        length = len(nums)
        if(length==0):
            return None
        else:
            node = TreeNode()
            node.val= nums[length//2]
            node.left =self.sortedArrayToBST(nums[:length//2])
            node.right = self.sortedArrayToBST(nums[length//2 +1:])    
        return node
            
if __name__ == "__main__":
    a = [3]
    print(a[1:])