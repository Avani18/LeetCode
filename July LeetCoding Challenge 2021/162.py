# Find Peak Element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l = len(nums)
        
        if l == 1:
            return 0
        
        nums.insert(0, float('-inf'))
        nums.insert(l+1, float('-inf'))
        
        l = len(nums)
        
        for i in range(1, l-1):
            if (nums[i] > nums[i-1] and nums[i] > nums[i+1]):
                return i-1
