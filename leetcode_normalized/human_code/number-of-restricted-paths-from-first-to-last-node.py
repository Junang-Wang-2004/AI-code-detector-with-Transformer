import heapq

class C1(object):

    def countRestrictedPaths(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[] for v3 in range(a1)]
        for v4, v5, v6 in a2:
            v2[v4 - 1].append((v5 - 1, v6))
            v2[v5 - 1].append((v4 - 1, v6))
        v7 = [float('inf')] * a1
        v8 = [0] * a1
        v7[a1 - 1] = 0
        v8[a1 - 1] = 1
        v9 = [(0, a1 - 1)]
        while v9:
            v6, v4 = heapq.heappop(v9)
            if v6 > v7[v4]:
                continue
            for v5, v10 in v2[v4]:
                if v6 + v10 < v7[v5]:
                    v7[v5] = v6 + v10
                    heapq.heappush(v9, (v7[v5], v5))
                elif v6 > v7[v5]:
                    v8[v4] = (v8[v4] + v8[v5]) % v1
            if v4 == 0:
                break
        return v8[0]
