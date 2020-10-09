# Edit Distance

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