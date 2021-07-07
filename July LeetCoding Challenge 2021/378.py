# Kth Smallest Element in a Sorted Matrix

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        flat = []
        for i in range(len(matrix)):
            flat += matrix[i]

        flat.sort()
        return flat[k-1]
