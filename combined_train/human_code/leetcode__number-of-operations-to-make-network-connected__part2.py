import collections

class C1(object):

    def makeConnected(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            if a1 in a2:
                return 0
            a2.add(a1)
            if a1 in G:
                for v1 in G[a1]:
                    dfs(v1, a2)
            return 1
        if len(a2) < a1 - 1:
            return -1
        v1 = collections.defaultdict(list)
        for v2, v3 in a2:
            v1[v2].append(v3)
            v1[v3].append(v2)
        v4 = set()
        return sum((dfs(v2, v4) for v2 in range(a1))) - 1
