# Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/
# Given a positive integer num, write a function which returns True if num is a perfect square else False. Note: Do not use any built-in library function such as sqrt.

def isPerfectSquare(num):
        
        x = num ** 0.5
        if (x == int(x)):
            return True
        else:
            return False
            
print (isPerfectSquare(16))
