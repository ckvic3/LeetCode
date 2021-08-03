# Shuffle an Array

from typing import List

import random
import copy
class Solution:

    def __init__(self, nums: List[int]):
        
        self.nums = nums
        self.array = copy.deepcopy(nums)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array =  copy.deepcopy(self.nums)
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """

        for i in range(len(self.array)-1,0,-1):

            index = random.randint(0,i)
            temp = self.array[i]
            self.array[i] = self.array[index]
            self.array[index] = temp
            
        return self.array


if __name__ == "__main__":
    pass