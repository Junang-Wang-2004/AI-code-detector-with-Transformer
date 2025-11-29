import heapq

class C1(object):

    def minimumDifference(self, a1):
        v1 = len(a1)
        v2 = v1 // 3
        v3 = [0] * (v2 + 1)
        v4 = []
        v5 = 0
        for v6 in range(v2):
            v7 = a1[v6]
            heapq.heappush(v4, -v7)
            v5 += v7
        v3[0] = v5
        for v8 in range(1, v2 + 1):
            v7 = a1[v2 + v8 - 1]
            v9 = heapq.heappushpop(v4, -v7)
            v10 = -v9
            v5 += v7 - v10
            v3[v8] = v5
        v11 = [0] * (v2 + 1)
        v12 = []
        v13 = 0
        for v6 in range(v1 - v2, v1):
            v7 = a1[v6]
            heapq.heappush(v12, v7)
            v13 += v7
        v11[0] = v13
        for v8 in range(1, v2 + 1):
            v7 = a1[2 * v2 - v8]
            v14 = heapq.heappushpop(v12, v7)
            v13 += v7 - v14
            v11[v8] = v13
        v15 = float('inf')
        for v6 in range(v2 + 1):
            v15 = min(v15, v3[v6] - v11[v2 - v6])
        return v15
