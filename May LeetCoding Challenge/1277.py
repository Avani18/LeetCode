# Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

def countSquares(matrix):
        total_squares = 0
        i = 0
        
        while i < len(matrix):
            j = 0
            while j < len(matrix[0]):
                if matrix[i][j]:
                    if i == 0 or j == 0:
                        total_squares += 1
                    else:
                        squares = min(matrix[i][j-1],
                                      matrix[i-1][j],
                                      matrix[i-1][j-1]) + 1
                        total_squares += squares
                        matrix[i][j] = squares
                j += 1
            i += 1
        return total_squares

print (countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))
