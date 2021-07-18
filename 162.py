# Find Peak Element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # Neighbours = all neighbours (not just immediate)
        
        left, right = 0, len(nums) - 1
        
        while (left < right):
            
            mid = left + (right - left)//2
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
                
            else:
                right = mid
        
        return right
    
    
        #return nums.index(max(nums))
