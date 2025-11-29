import collections

class C1(object):

    def longestSpecialPath(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            v1, lookup[a2[a1] - 1] = (lookup[a2[a1] - 1], a3)
            a4 = max(a4, v1)
            result[0] = min(result[0], [-(prefix[a3 - 1 + 1] - prefix[a4 + 1]), a3 - a4])
            for v3, v4 in adj[a1]:
                if v3 == a2:
                    continue
                prefix.append(prefix[-1] + v4)
                dfs(v3, a1, a3 + 1, a4)
                prefix.pop()
            lookup[a2[a1] - 1] = v1
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = collections.defaultdict(lambda: -1)
        v7 = [0]
        v8 = [[float('inf'), float('inf')]]
        dfs(0, -1, 0, -1)
        return [-v8[0][0], v8[0][1]]
