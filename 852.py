# Peak Index in a Mountain Array


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))        
