# H-Index II
# https://leetcode.com/problems/h-index-ii/
'''Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, 
and the other N − h papers have no more than h citations each."'''


def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n , left , right = len(citations) , 0 , len(citations)
        while left < right:
            mid = left + (right - left) // 2
            numGreater = n - mid
            if numGreater <= citations[mid]:
                right = mid
            else:
                left = mid + 1
        return n - left