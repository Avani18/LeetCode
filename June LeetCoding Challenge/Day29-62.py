# Unique Paths
# https://leetcode.com/problems/unique-paths/
'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?'''


def uniquePaths(self, m: int, n: int) -> int:
        n,k=n+m-2,m-1
        count=min(n-k,k)
        up=down=1
        while count>0:
            up*=n
            down*=count
            n-=1
            count-=1
        return up//down
