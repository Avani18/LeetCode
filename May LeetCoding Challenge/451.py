# Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/
# Given a string, sort it in decreasing order based on the frequency of characters.

from collections import Counter

def frequencySort(s):
        
        count = Counter(s)
        st = ''
        count = count.most_common()
        for item, counts in count:
            st += item*counts
        return st

print (frequencySort('tree'))
