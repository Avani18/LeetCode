# Contiguous Array
# https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3341/
#Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.


def findMaxLength(self, nums: List[int]) -> int:
        
        s=0
        m=0
        c=0
        d={0:-1}
        for i in nums:
            if i==0:
                s=s+1
            else:
                s=s-1
            if s not in d:
                d[s]=c
            else:
                m=max(m,c-d[s])
            c+=1
        return m
