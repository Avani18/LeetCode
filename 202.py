# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getDigits(n):
            dig = []
            while n:
                dig.append(n%10)
                n //= 10
            return dig
        
        done = []
        
        while True:
            dig = getDigits(n)
            n = sum([i*i for i in dig])
            if n in done:
                return False
            done.append(n)
            
            if n == 1:
                return True
            else:
                continue 
