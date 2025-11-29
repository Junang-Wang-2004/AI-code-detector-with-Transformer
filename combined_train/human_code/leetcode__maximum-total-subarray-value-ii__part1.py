import heapq

class C1(object):

    def maxTotalValue(self, a1, a2):
        """
        """

        def nxt(a1, a2, a3, a4):
            while not a1 <= idxs[a3] <= a2:
                a3 += 1
            while not a1 <= idxs[a4] <= a2:
                a4 -= 1
            return (a3, a4)
        v1 = list(range(len(a1)))
        v1.sort(key=lambda x: (a1[x], x))
        v2 = {(0, len(a1) - 1): (0, len(v1) - 1)}
        v3 = [(-(a1[v1[len(v1) - 1]] - a1[v1[0]]), (0, len(v1) - 1))]
        v4 = 0
        while a2:
            v5, (v6, v7) = heapq.heappop(v3)
            v8, v9 = v2[v6, v7]
            v10, v11 = (min(v1[v8], v1[v9]), max(v1[v8], v1[v9]))
            v12 = min((v10 - v6 + 1) * (v7 - v11 + 1), a2)
            a2 -= v12
            v4 += v12 * -v5
            if v10 + 1 <= v7 and (v10 + 1, v7) not in v2:
                v2[v10 + 1, v7] = v14, v15 = nxt(v10 + 1, v7, v8, v9)
                heapq.heappush(v3, (-(a1[v1[v15]] - a1[v1[v14]]), (v10 + 1, v7)))
            if v6 <= v11 - 1 and (v6, v11 - 1) not in v2:
                v2[v6, v11 - 1] = v14, v15 = nxt(v6, v11 - 1, v8, v9)
                heapq.heappush(v3, (-(a1[v1[v15]] - a1[v1[v14]]), (v6, v11 - 1)))
        return v4
