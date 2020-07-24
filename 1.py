# Two Sum
# https://leetcode.com/problems/two-sum/
'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.'''


def twoSum(self, nums: List[int], target: int) -> List[int]:
        
	final_dict = {}
        
	for i in range(len(nums)):        
		diff = target - nums[i]
		if diff in final_dict:
			return final_dict[diff], i
		else:
			final_dict[nums[i]] = i 