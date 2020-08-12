# Course Schedule

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = [0]*numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a]+=1
        queue = collections.deque([course for course,ind in enumerate(indegree) if ind==0])
        while queue:
            course = queue.popleft()
            numCourses-=1
            for nei in graph[course]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return numCourses==0