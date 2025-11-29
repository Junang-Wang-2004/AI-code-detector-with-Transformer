# Time:  O(|V| + |E|)
# Space: O(|E|)
import collections


# dfs solution
class Solution3(object):
    def findOrder(self, numCourses, prerequisites):
        """
        """
        WHITE, GRAY, BLACK = list(range(3))
        def dfs(u):
            if lookup[u] != WHITE:
                return lookup[u] == BLACK
            lookup[u] = GRAY
            if any(not dfs(v) for v in adj[u]):
                return False
            lookup[u] = BLACK
            result.append(u)  # should be postorder
            return True

        result = []
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
        lookup = collections.defaultdict(lambda:WHITE)
        for u in range(numCourses):
            if not dfs(u):
                return []
        return result

    
