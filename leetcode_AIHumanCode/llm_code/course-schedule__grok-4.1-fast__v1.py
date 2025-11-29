from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for to, fr in prerequisites:
            graph[fr].append(to)
        
        visit = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
        
        def has_cycle(node: int) -> bool:
            if visit[node] == 1:
                return True
            if visit[node] == 2:
                return False
            visit[node] = 1
            for neigh in graph[node]:
                if has_cycle(neigh):
                    return True
            visit[node] = 2
            return False
        
        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
