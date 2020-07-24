# Palindrome Number
# https://leetcode.com/problems/palindrome-number/
'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''


def isPalindrome(self, x: int) -> bool:

	#Without conversion to string 
        reverse = 0 
        og = x
        while (x>0):
            reverse = (reverse*10) + (x%10)
            x //= 10
        if reverse == og:
            return True 
        else:
            return False
			
	#Conversion to string appraoch 
        '''if str(x) == str(x)[::-1]:
            return True 
        else:
            return False'''