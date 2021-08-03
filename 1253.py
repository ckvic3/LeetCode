# Reconstruct a 2-Row Binary Matrix
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        
        if upper + lower != sum(colsum):
            return []

        upper, lower = max(upper,lower),min(upper,lower)
        matrix = [[],[]]
        enumerate
        for i in range(len(colsum)):
            if colsum[i]==2:
                matrix[0].append(1)
                lower -= 1
                matrix[1].append(1)
                upper -= 1
            elif colsum[i]==0:
                matrix[0].append(0)
                matrix[1].append(0)    
            else:
                if(lower>0):
                    matrix[0].append(1)
                    matrix[1].append(0)
                    lower -= 1
                else:
                    matrix[0].append(0)
                    matrix[1].append(1)
                    upper -= 1

        return matrix    

