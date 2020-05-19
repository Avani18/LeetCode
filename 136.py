# Single Number
# https://leetcode.com/problems/single-number/
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
 
def singleNumber(nums):
	for i in nums:
		if (nums.count(i)==1):
			return i
print (singleNumber([2,2,1]))
