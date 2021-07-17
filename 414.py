# Third Maximum Number

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        
        if(len(nums)<3):
            return max(nums)
        
        return sorted(nums, reverse = True)[2]
