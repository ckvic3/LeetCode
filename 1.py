# Two Sum

from typing import List

# version 1 
# time: o(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                   return [i,j] 

# version 2
# time: o(n)           
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexing = {}

        for i in range(len(nums)):
            if(nums[i] in indexing.keys()):
                if(indexing[nums[i]] != i):
                    return [i, indexing[nums[i]]]
            else:
                indexing[target-nums[i]] = i