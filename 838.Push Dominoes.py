# 838 Push Dominoes

# version 1: 
# time : o(n)
# memory: o(1)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        length = len(dominoes)
        dominoes = list(dominoes)
        pr = length
        pl = -1
        pf = 0
        for i in range(length):
            if(dominoes[i] == 'L'):
                pl = i 
                if(pr!=length):  # 在当前L之前存在R,则对两者之间根据距离进行处理。
                    temp = (pl- pr + 1)//2
                    for j in range(temp):
                        dominoes[pr+j] = 'R'
                        dominoes[pl-j] = 'L'
                    pr = length
                else:  # 在当前的L之前不存在R，可以将当前L之前到锚点之前的全部变为L
                    for j in range(pf,pl,1):
                        dominoes[j] = 'L'
                pl = -1  # 将pl重设为原始值
                pf = i + 1 # 处理完毕长度更新

            elif(dominoes[i] == 'R'):
                if(pr<i): # 在当前R之前不存在L而存在一个R，则将两个R之间的元素全部变为R
                    for j in range(pf,i):
                        dominoes[j] = 'R'
                pf = i + 1 # 处理完毕长度更新
                pr = i # 更新pr
                
                
        if(pr!=length):
            for i in range(pr,length):
                dominoes[i] = 'R'
        # if(pl!=-1):
        #     for i in range(pf,pl):
        #         dominoes[i] = 'L'

        return "".join(dominoes)

# version 2
class Solution:  
    def pushDominoes(self, dominoes: str) -> str:
            dominoes = list(dominoes)
            dominoes.append('R')
            
            prev = 'L'
            prevIndex = 0
            for i, x in enumerate(dominoes):
                if(x != '.'):
                    if(x==prev):
                        for j in range(prevIndex,i+1,1):
                            dominoes[j] = x
                    else:
                        if(prev == 'R'):
                            temp = (i - prevIndex - 1) //2
                            for j in range(temp):
                                dominoes[prevIndex+j+1] = 'R'
                                dominoes[i-j-1] = 'L'
                    prevIndex = i        
                    prev = x
                        
            return "".join(dominoes[:-1])


if __name__ =="__main__":
    method = Solution()
    # strs = ".L.R...LR..L.."
    strs = ".RR..LL.."
    strs = method.pushDominoes(strs)
    print(strs)