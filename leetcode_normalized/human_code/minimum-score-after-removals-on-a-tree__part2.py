from functools import reduce

class C1(object):

    def minimumScore(self, a1, a2):
        """
        """

        def is_ancestor(a1, a2):
            return left[a1] <= left[a2] and right[a2] <= right[a1]

        def dfs(a1, a2):
            left[a1] = cnt[0]
            cnt[0] += 1
            for v1 in adj[a1]:
                if v1 == a2:
                    continue
                dfs(v1, a1)
                a1[a1] ^= a1[v1]
            right[a1] = cnt[0]
        v1 = [[] for v2 in range(len(a1))]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [0]
        v6 = [0] * len(a1)
        v7 = [0] * len(a1)
        dfs(0, -1)
        v8 = float('inf')
        for v9 in range(1, len(a1)):
            for v10 in range(v9 + 1, len(a1)):
                if is_ancestor(v9, v10):
                    v11, v12, v13 = (a1[0] ^ a1[v9], a1[v9] ^ a1[v10], a1[v10])
                elif is_ancestor(v10, v9):
                    v11, v12, v13 = (a1[0] ^ a1[v10], a1[v10] ^ a1[v9], a1[v9])
                else:
                    v11, v12, v13 = (a1[0] ^ a1[v9] ^ a1[v10], a1[v9], a1[v10])
                v8 = min(v8, max(v11, v12, v13) - min(v11, v12, v13))
        return v8
