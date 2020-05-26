# First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

import collections

def firstUniqChar(s):
        
        count = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1
        
print (firstUniqChar('leetcode'))
