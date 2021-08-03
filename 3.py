# Longest Substring Without Repeating Characters
from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s:str) ->int:
        record = {}
        maxLength = 0
        Length = 0
        if(len(s) == 0):
            return maxLength

        for i, char in enumerate(s):
            if char not in record.keys():
                Length = Length + 1
                record[char] = i
            else:
                if (i - record[char] > Length):
                    Length = Length + 1
                else:
                    Length = i - record[char] 
            
            if(Length>maxLength):
                maxLength = Length

        return maxLength