# Perfect Squares
# https://leetcode.com/problems/perfect-squares/
'''Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.'''


def numSquares(self, n: int) -> int:
        dp = [0] + [float('inf')] * (n)
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]
