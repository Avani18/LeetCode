# Single Element in a Sorted Array
# https://leetcode.com/problems/single-element-in-a-sorted-array/
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

from collections import Counter

def singleNonDuplicate(nums):
        counter = Counter(nums)
        return list(counter.keys())[list(counter.values()).index(1)]
        
print (singleNonDuplicate([1,1,2,3,3,4,4,8,8]))
