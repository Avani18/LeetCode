# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

def checkInclusion(s1, s2):
        
        lenS1 = len(s1)
        lenS2 = len(s2)
        if lenS1 > lenS2:
            return False
        frequency = {} # {char:count}, we will decrease/increase the num of letters we are still awaiting in the window 
        left, matсhes = 0, 0
        # put chars from s1 into dict for O(n) access per char
        for i in range(lenS1):
            if s1[i] in frequency:
                frequency[s1[i]] += 1 # s1 can contain similar letters
            else:
                frequency[s1[i]] = 1
        # sliding window
        for right in range(lenS2):
            current = s2[right]
            isIn = current in frequency
			# try to reduce the window or break if we can accept this char
            while left <= right:
                if isIn and frequency[current] > 0: # we are ok to accept this possibly duplicated letter
                    matсhes += 1
                    frequency[current] -= 1
                    break
                else:
                    if s2[left] in frequency:
                        if frequency[s2[left]] >= 0:
                            matсhes -= 1
                        frequency[s2[left]] += 1
                    left += 1 # reduce the window from left
            if matсhes == lenS1:
                return True
        return False
        
print(checkInclusion('ab', 'eidbaooo'))
