# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        totalSum = 0
        for x in enumerate(str):
            if map[x] > prev:
                totalSum = totalSum - prev
               
            else:
                totalSum = totalSum + prev
            prev = map[x]
        return totalSum + prev
        