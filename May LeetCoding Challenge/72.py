# Edit Distance
# https://leetcode.com/problems/edit-distance/
'''Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character'''


def minDistance(self, word1: str, word2: str) -> int:
        dp = [[float('inf')]*(len(word2)+1) for i in range(len(word1)+1)]
        dp[0][0] = 0
        
        for i in range(1, len(dp)):
            dp[i][0] = i
        
        for j in range(1, len(dp[0])):
            dp[0][j]  = j
            
        
        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                    pass
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        return dp[-1][-1]
