# Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/
''' In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1. '''

def findJudge(N, trust):
        
        trust_score = [0] * (N + 1)
        for a,b in trust:
            trust_score[a] -= 1
            trust_score[b] += 1
            
        for i in range(1, len(trust_score)):
            if (trust_score[i] == N - 1):
                return i 
            
        return -1
        
print (findJudge(2, [[1,2]]))
