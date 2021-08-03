# Non-negative Integers without Consecutive Ones

class Solution:
    def findIntegers(self, n: int) -> int:
        if(n<3):
            return n+1
        elif(n==3):
            return 3
        temp = n
        binary = []
        while(temp!=0):
            binary.append(temp%2)
            temp = temp // 2
        print(binary)
        length = len(binary)
            
        numbers = [0]* length
        for i in range(2,length):
            numbers[i] = numbers[i-1]*2 + pow(2,max(i-3,0)) - numbers[i-3]
        print(numbers)


        TotalRightNumbers = 0
        prev = 0
        currentNumbers = 0
        for i in range(length-1,-1,-1):
            if(binary[i]==1):
                currentNumbers += pow(2,i)  # 上限数字不断增大
            if(binary[i]==1 and prev == 1):
                TotalRightNumbers += n - currentNumbers + 1 # 当前一个数字为1，且当前数字为1.则将后面的所有数字都可当作符合条件的数字。返回即可
                TotalRightNumbers += numbers[i]
                break
            elif(binary[i]==0):     # 前一个数字为1，当前数字为0，
                prev = 0
            elif(binary[i]==1):     # 前一个数字为0，当前数字为1. 计算从currentNumber 到 currentNumber + pow(2,i)之间符合要求的数字
                TotalRightNumbers += numbers[i]
                prev = 1
            print(TotalRightNumbers)
        print(n + 1 - TotalRightNumbers)    
        return n + 1 - TotalRightNumbers

                


if __name__=="__main__":
    method = Solution()
    method.findIntegers(11)