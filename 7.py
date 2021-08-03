# Reverse Integer 
# not complete

class Solution:
    def reverse(self, x: int) -> int:
        max = 2147483647
        min = -2147483648
        flag = False
        if(x == min):
            return 0
        elif(x <0):
            x = -x
            flag = True

        smallMax = max /10
        smallMin = min /10
        temp = []
        while(x !=0):
            temp.append(x%10)
            x = x // 10
                
            print(x)
        result = 0
        
        newFlag = True
        for item in temp:
            if(newFlag and item == 0 ):
                continue
            else:
                newFlag = False
                result = result * 10 + item
                if(not flag and result>smallMax):
                    return 0
                elif(flag and result<smallMin):
                    return 0
        if(flag):
            result = - result
        return result
        
soultion = Solution()
result = soultion.reverse(901000)

print(result)