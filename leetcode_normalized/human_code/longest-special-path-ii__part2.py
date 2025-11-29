import collections

class C1(object):

    def longestSpecialPath(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            v1, lookup[a2[a1] - 1] = (lookup[a2[a1] - 1], a3)
            v2 = a4[:]
            v3 = v1
            for v4 in range(len(v2)):
                if v3 > v2[v4]:
                    v3, v2[v4] = (v2[v4], v3)
            result[0] = min(result[0], [-(prefix[a3 - 1 + 1] - prefix[v2[1] + 1]), a3 - v2[1]])
            for v5, v6 in adj[a1]:
                if v5 == a2:
                    continue
                prefix.append(prefix[-1] + v6)
                dfs(v5, a1, a3 + 1, v2)
                prefix.pop()
            lookup[a2[a1] - 1] = v1
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4, v5 in a1:
            v1[v3].append((v4, v5))
            v1[v4].append((v3, v5))
        v6 = collections.defaultdict(lambda: -1)
        v7 = [0]
        v8 = [[float('inf'), float('inf')]]
        dfs(0, -1, 0, [-1] * 2)
        return [-v8[0][0], v8[0][1]]
