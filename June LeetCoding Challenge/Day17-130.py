# Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
'''Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.'''


def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m <= 1:
		    return
        n = len(board[0])

        moves = [[0, 1],[1, 0],[-1, 0],[0, -1]]


        def dfs(i, j):
			if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
				board[i][j] = '#'

				for p, q in moves:
					dfs(i+p, j+q) 

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1 and board[i][j] == 'O':
                    dfs(i, j)

        board[:] = [['XO'[c == '#'] for c in row] for row in board]