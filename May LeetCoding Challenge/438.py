# Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
''' Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.'''

import string

def findAnagrams(s, p):
        def counter(s):
            return [s.count(c) for c in string.ascii_lowercase]

        ans=[]
        counts = counter(s[:len(p)])
        target = counter(p)
        if counts == target:
            ans.append(0)
        for i, c in enumerate(s[len(p):]):
            counts[ord(s[i])-ord('a')] -= 1
            counts[ord(c)-ord('a')] += 1
            if counts == target:
                ans.append(i+1)
        return ans
        
print (findAnagrams('cbaebabacd', 'abc'))
