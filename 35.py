# Search Insert Position 

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