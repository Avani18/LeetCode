# Maximum Product Difference Between Two Pairs

class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Solution 1
        nums.sort()
        return ((nums[-1]*nums[-2]) - (nums[1]*nums[0]))
    
        # Solution 2
#         n1 = max(nums)
#         nums.remove(n1)
#         n2 = min(nums)
#         nums.remove(n2)
        
#         return ((n1 * max(nums)) - (n2 * min(nums)))
