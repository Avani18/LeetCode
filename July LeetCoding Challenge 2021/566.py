# Reshape the Matrix

class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        rows_i = len(mat)
        cols_i = len(mat[0])

        if ((rows_i * cols_i) != (r * c)):
            return mat

        # Solution1
#         res = [[]*c for _ in range(r)]
#         nums = [j for sub in mat for j in sub]

#         cnt = 0
#         for i in range(r):
#             for j in range(c):
#                 res[i].append(nums[cnt])
#                 cnt += 1
#         return res

        # Solution 2
        res = []
        nums = []
        for i in range(rows_i):
            nums += mat[i]

        for i in range(r):
            res.append(nums[i*c:(i+1)*c])

        return res
