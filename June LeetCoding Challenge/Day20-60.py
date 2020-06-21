# Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/
'''The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.'''

def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1,n+1))
        answer = ""
        
        for n_it in range(n,0,-1):
            d = (k-1)//factorial(n_it-1)
            k -= d*factorial(n_it-1)
            answer += str(numbers[d])
            numbers.remove(numbers[d])
                   
        return answer