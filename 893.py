from typing import List
import numpy as np
def getCounts(str):        
    counts = []
    counts.append(np.zeros(26))
    counts.append(np.zeros(26))
    for i,c in enumerate(str):
        counts[i%2][ord(c)-97] +=1

    return counts


def equals(counts1,groups):
    for counts2 in groups:
        if(np.array_equal(counts1[0],counts2[0]) and np.array_equal(counts1[1],counts2[1])):
            return True
        
    return False

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:

        totoalGroup = 0
        groups = []
        for i in range(len(words)):
            counts = getCounts(words[i])
            if len(groups)==0:
                groups.append(counts)
            else:
                if(not equals(counts, groups)):
                    groups.append(counts)
                        
        return len(groups)       