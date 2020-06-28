# Reconstruct Itinerary
# https://leetcode.com/problems/reconstruct-itinerary/
'''Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.'''


def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ans = []
        stack = ["JFK"]

        dic = {}

        for i in range(len(tickets)):
            if(tickets[i][0] in dic):
                dic[tickets[i][0]].append(tickets[i][1])
            else:
                dic[tickets[i][0]] = [tickets[i][1]]
        
        for i in dic:
            dic[i].sort()

        while(stack):
            curr = stack[-1]
            if curr in dic and len(dic[curr])>0:
                stack.append(dic[curr].pop(0))
            else:
                ans.append(stack.pop())
        
        return(ans[::-1])
