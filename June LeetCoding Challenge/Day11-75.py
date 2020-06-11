# Sort Colors
# https://leetcode.com/problems/sort-colors/
'''Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.'''

def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0:0, 1:0, 2:0}
        
        ptr = [0]*3
        
        for i, x in enumerate(nums):
            counter[x] += 1
            nums[ptr[x]] = x
            ptr[x] += 1
            for j in range(x+1, 3):
                if counter[j] > 0:
                    nums[ptr[j]] = j
                ptr[j] += 1
