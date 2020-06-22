# Single Number II
# https://leetcode.com/problems/single-number-ii/
'''Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.'''


from collections import Counter 

def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        return list(count.keys())[list(count.values()).index(1)]