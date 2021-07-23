# Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)
        l.append('Z')
        num = 0
        i = 0
        while i < len(l):
            print(i)
            if l[i] == 'M':
                num += 1000
                
            elif l[i] == 'D':
                num += 500
                
            elif l[i] == 'L':
                num += 50
                
            elif l[i] == 'V':
                num += 5
                
            elif l[i] == 'C' and l[i+1] == 'D':
                num += 400
                i += 1
                
            elif l[i] == 'C' and l[i+1] == 'M':
                num += 900
                i += 1
                
            elif l[i] == 'C':
                num += 100
                
            elif l[i] == 'X' and l[i+1] == 'L':
                num += 40
                i += 1
                
            elif l[i] == 'X' and l[i+1] == 'C':
                num += 90
                i += 1
            
            elif l[i] == 'X':
                num += 10

            elif l[i] == 'I' and l[i+1] == 'V':
                num += 4
                i += 1
                
            elif l[i] == 'I' and l[i+1] == 'X':
                num += 9
                i += 1
                
            elif l[i] == 'I':
                num += 1
                
            i += 1
                
        return num
