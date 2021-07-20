# Shuffle An Array

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums.copy()
        self.l = nums.copy()

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.l = self.nums.copy()
        return self.l
        

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.l)
        return self.l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
