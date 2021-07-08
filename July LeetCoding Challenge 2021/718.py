# Maximum Length of Repeated Subarray


class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        g_max = 0
        
        dp = [[0 for _ in range(len(nums1) + 1)] for _ in range(len(nums2) + 1)]
        
        for i in range(1,len(nums2)+1):
            for j in range(1,len(nums1)+1):
                if (nums2[i-1] == nums1[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                    g_max = max(g_max, dp[i][j])

        return g_max
