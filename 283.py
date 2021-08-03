# 283. Move Zeroes
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
       
        for i in range(len(nums)):
            if(nums[i]!=0):
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j = j + 1

if __name__ == "__main__":
    method = Solution()
    method.moveZeroes([2,1])
                  
