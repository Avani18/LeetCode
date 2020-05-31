# Maximum Sum Circular Subarray
# https://leetcode.com/problems/maximum-sum-circular-subarray/
''' Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)'''

def maxSubarraySumCircular(A):
        max_best = -float(inf)
        max_curr = -float(inf)
        min_best = float(inf)
        min_curr = float(inf)
        
        tot = 0
        
        for n in A:
            max_curr = max(max_curr, 0) + n
            min_curr = min(min_curr, 0) + n
            max_best = max(max_best, max_curr)
            min_best = min(min_best, min_curr)
            tot += n
            
        if max_best < 0:
            return max_best
            
        return max(max_best, tot - min_best)
        
print (maxSubarraySumCircular([1, -2, 3, -2]))
