# Time:  O(|E| + |V|)
# Space: O(|V|)
import collections


class Solution2(object):
    def makeConnected(self, n, connections):
        """
        """
        def dfs(i, lookup):
            if i in lookup:
                return 0
            lookup.add(i)
            if i in G:
                for j in G[i]:
                    dfs(j, lookup)
            return 1

        if len(connections) < n-1:
            return -1
        G = collections.defaultdict(list)
        for i, j in connections:
            G[i].append(j)
            G[j].append(i)
        lookup = set()
        return sum(dfs(i, lookup) for i in range(n)) - 1
