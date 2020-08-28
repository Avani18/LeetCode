# Uncrossed Lines
# https://leetcode.com/problems/uncrossed-lines/
'''We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.'''

def maxUncrossedLines(A, B):
        m, n = len(A), len(B)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], 1 + dp[i][j])
        return dp[-1][-1]

print (maxUncrossedLines([1,4,2], [1,2,4]))
                    
