# Time:  O(|V| + |E|)
# Space: O(|E|)
import collections


# dfs solution
class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        """
        adj = collections.defaultdict(list)
        in_degree = collections.Counter()
        for u, v in prerequisites:
            in_degree[u] += 1
            adj[v].append(u)
        result = []
        stk = [u for u in range(numCourses) if u not in in_degree]
        while stk:
            u = stk.pop()
            result.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    stk.append(v)
        return len(result) == numCourses
