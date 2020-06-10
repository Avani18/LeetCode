# Search Insert Position
# https://leetcode.com/problems/search-insert-position/
'''Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.'''


def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target in nums:
            return nums.index(target)

        if target > max(nums):
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] < target:
                continue
            else:
                return i
