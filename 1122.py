# Relative Sort Array
from typing import KeysView, List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        newList = []
        
        numbers = {}
        for x in arr2:
            numbers[x] = 0
        
        for x in arr1:
            if x in arr2:
                numbers[x]+=1
            else:
                newList.append(x)
        
        newList.sort()

        results = []
        for x in arr2:
            for j in range(numbers[x]):
                results.append(x)
        
        for x in newList:
            results.append(x)
        print(results)
        return results

        



if __name__ == "__main__":
    pass
            