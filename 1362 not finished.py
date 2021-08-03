# Closest Divisors
import math
# 时间复杂度过高
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        
        query = num + 1 
        middle = math.sqrt(query)
        middle = int(middle)
        low = middle
        high = middle
        while(low*high!=query):
            
            if low * high < query:
                high = high + 1
                low = query // high
            else:
                low = low - 1
                high = query // low

        cloest = high - low
        result = [low,high]
        query = num+2
        middle = math.sqrt(query)
        middle = int(middle)
        low = middle
        high = middle
        while(low*high!=query):
            if low * high < query:
                high = high + 1
                low = query // high
            else:
                low = low - 1
                high = query // low

        if(high - low > cloest):
            result = [low,high]
        
        return result



        