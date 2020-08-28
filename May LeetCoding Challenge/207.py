# Course Schedule
# https://leetcode.com/problems/course-schedule/
'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?'''


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
