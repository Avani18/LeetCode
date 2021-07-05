#Monotonic Array


class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(set(nums))) == 1:
            return True
        if sorted(nums) == nums or sorted(nums, reverse = True) == nums:
            return True
        return False
