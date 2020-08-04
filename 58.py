# Length of Last Word

def lengthOfLastWord(self, s: str) -> int:
        if s=='':
            return 0
        while s!='' and s[-1]==' ':
            s=s[:-1]
        if s=='':
            return 0
        count=0
        while s!='' and s[-1]!=' ':
            count+=1
            s=s[:-1]
        return count