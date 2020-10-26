# Count Negative Numbers in a Sorted Matrix


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        neg = 0
        a = len(grid)
        b = len(grid[0])
        for i in range(a):
            for j in range(b -1, -1, -1):
                if grid[i][j] < 0:
                    neg += 1
                else:
                    break
                    
        return neg
