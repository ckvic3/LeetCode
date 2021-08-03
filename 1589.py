# Maximum Sum Obtained of Any Permutation

from typing import List

import numpy as np
 
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        length = len(nums)
        list.sort(nums,reverse=True)
        nums = np.array(nums)
        counts = np.zeros([length])
        for request in requests:    
            counts[request[0]:request[1]+1] += 1

        counts = abs(np.sort(-counts))   

        sums = nums* counts

        return int(sums.sum())
               


          
        