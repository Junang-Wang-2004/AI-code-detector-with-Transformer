import heapq

class C1(object):

    def minTime(self, a1, a2, a3, a4, a5):
        """
        """

        def update(a1, a2, a3, a4, a5):
            v1 = lookup[a5] * a5[a3]
            v2 = a2 ^ 1
            v3 = (a3 + int(v1)) % a3
            v4 = a4 ^ a5
            v5 = a1 + v1
            if dist[v2][v3][v4] > v5:
                dist[v2][v3][v4] = v5
                heapq.heappush(min_heap, (v5, v2, v3, v4))
        v1 = [0] * (1 << a1)
        for v2 in range(1, 1 << a1):
            v1[v2] = v1[v2 >> 1] + (v2 & 1)
        v3 = [max((a4[v2] for v2 in range(a1) if mask & 1 << v2)) if mask else 0 for v4 in range(1 << a1)]
        v5 = float('inf')
        v6 = [[[v5] * (1 << a1) for v7 in range(a3)] for v7 in range(2)]
        v6[0][0][(1 << a1) - 1] = 0.0
        v8 = [(0.0, 0, 0, (1 << a1) - 1)]
        while v8:
            v9, v10, v11, v4 = heapq.heappop(v8)
            if v9 != v6[v10][v11][v4]:
                continue
            if v4 == 0:
                assert v10 == 1
                return v9
            if v10 == 0:
                v12 = v4
                while v12:
                    if v1[v12] <= a2:
                        update(v9, v10, v11, v4, v12)
                    v12 = v12 - 1 & v4
            else:
                for v2 in range(a1):
                    if v4 & 1 << v2:
                        continue
                    update(v9, v10, v11, v4, 1 << v2)
        return -1.0
