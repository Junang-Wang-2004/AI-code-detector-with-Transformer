import collections

class C1(object):

    def findOrder(self, a1, a2):
        """
        """
        v1, v2, v3 = list(range(3))

        def dfs(a1):
            if lookup[a1] != v1:
                return lookup[a1] == v3
            lookup[a1] = v2
            if any((not dfs(v) for v1 in adj[a1])):
                return False
            lookup[a1] = v3
            result.append(a1)
            return True
        v4 = []
        v5 = collections.defaultdict(list)
        for v6, v7 in a2:
            v5[v7].append(v6)
        v8 = collections.defaultdict(lambda: v1)
        for v6 in range(a1):
            if not dfs(v6):
                return []
        v4.reverse()
        return v4
