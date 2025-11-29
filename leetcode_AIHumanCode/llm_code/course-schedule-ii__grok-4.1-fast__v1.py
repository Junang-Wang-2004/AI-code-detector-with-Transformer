from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        n = numCourses
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        for ai, bi in prerequisites:
            graph[bi].append(ai)
            indegree[ai] += 1
        queue = deque(i for i in range(n) if indegree[i] == 0)
        schedule = []
        while queue:
            course = queue.popleft()
            schedule.append(course)
            for dependent in graph[course]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        return schedule if len(schedule) == n else []
