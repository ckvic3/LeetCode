# 4 sums not finished


from typing import List, Mapping


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        result = []
        List.sort(nums,reverse=False)
        if(length<4):
            return result
        i = 0
        j = length-1

        while(i<j):
            newTarget = target- nums[i] - nums[j]
            p = i+1
            q = j-1
            print("i,j",i,j)
            while(p<q):
                print("p,q",p,q)
                if(nums[p] + nums[q] == newTarget):
                    result.append([nums[i], nums[p], nums[q], nums[j]])

                old_p = p
                old_q = q
                
                while(p<q and nums[p] == nums[old_p]):
                    p = p + 1
                if(p==q):
                    p = old_p
                    while(p<q and nums[q] == nums[old_q]):
                        q = q - 1
                    if(p==q):
                        q = old_q

                if(p==old_p and q == old_q):
                    break

            
            old_i = i
            old_j = j

            while(nums[i] == nums[old_i] and i<j):
                i = i + 1
            if(i==j):
                i = old_i
                while(nums[j] == nums[old_j] and i<j):
                    j = j - 1
                if(i==j):
                    j =old_j
            if(i==old_i and j == old_j):
                break      
        return result
            
if __name__ == '__main__':
    
    method = Solution()
    result = method.fourSum(
[1,0,-1,0,-2,2],0)
    print(result)