# Word Search II
# https://leetcode.com/problems/word-search-ii/
'''Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.'''


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not words: return None
        
        root = trie = {}
        for w in words:
            trie = root
            for c in w:
                if c in trie:
                    trie=trie[c]
                else:
                    trie[c]={}
                    trie=trie[c]
            trie['#'] = True
            
        m,n = len(board), len(board[0])
        self.res = []
        
        def dfs(i,j,trie,word):
            if i<0 or i>=m or j<0 or j>=n: return 
            c = board[i][j]
            word = word + c
            
            # current 
            if c not in trie or c == '*': return
            trie = trie[c]
            if '#' in trie and trie['#']==True:
                self.res.append(word)
                trie['#']=False
            
            # next 
            board[i][j]='*'
            dfs(i+1,j,trie,word)
            dfs(i-1,j,trie,word)
            dfs(i,j+1,trie,word)
            dfs(i,j-1,trie,word)
            board[i][j]=c
            
        for i in range(m):
            for j in range(n):
                dfs(i,j,root,'')
        return self.res