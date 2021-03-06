# Majority Element
# https://leetcode.com/problems/majority-element/
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times. You may assume that the array is non-empty and the majority element always exist in the array.

import collections

def majorityElement(nums):
        
        count = collections.Counter(nums)
        for key, vals in count.items():
            if (vals > (len(nums) // 2)):
                return key
                
print (majorityElement([3,2,3]))
