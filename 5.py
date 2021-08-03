# Valid Triangle Number

from typing import List

def solution(nums: List[int]) -> int:
    list.sort(nums)
    length = len(nums)
    count = 0
    if(length < 3):
        return count
    
    while(length >=3):
        c = nums[length-1]
        ib = length-2
        ia = 0
        while(ia<ib):
            if(nums[ia] + nums[ib] > c):
                ib = ib - 1
                count = count + ib - ia + 1
            else: 
                ia = ia + 1

        length = length - 1
    return count    
    

solution([2,2])             
        
        
        
            
            
         


        
