# Partition Array into Disjoint Intervals
#
# time : o(n)
# memory : o(n)
from typing import List

# class Solution:
#     def partitionDisjoint(self, nums: List[int]) -> int:
#         length = len(nums)
#         mins = [0] * length
#         maxVal = nums[0]
       
        
#         minVal = nums[-1]
#         for i in range(length,-1,-1):
#             minVal = min(minVal,nums[i])
#             mins[i] = minVal

#         for i in range(length):
#             maxVal = max(maxVal,nums[i])
#             if(maxVal <= mins[i+1]):
#                 return i+1 


# version 2 
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        length = len(nums)
        maxVal = nums[0]
        allmax = nums[0]
        solution = 1
        for i in range(1,length,1):
            if nums[i] < maxVal:
                maxVal = allmax
                solution = i + 1
            else:
                allmax = max(allmax, nums[i])
        return solution