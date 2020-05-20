# Number of steps to reduce a number to zero
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps (num):
        counter=0
        while(num):
            if (num%2==0):
                num/=2
                counter+=1
            else:
                num-=1
                counter+=1
        return counter
        
print(numberOfSteps(14))
