import heapq

class C1(object):

    def getBiggestThree(self, a1):
        """
        """
        v1 = 3
        v2 = [[a1[i][j] for v3 in range(len(a1[i]))] for v4 in range(len(a1))]
        v5 = [[a1[v4][v3] for v3 in range(len(a1[v4]))] for v4 in range(len(a1))]
        for v4 in range(1, len(a1)):
            for v3 in range(len(a1[0]) - 1):
                v2[v4][v3] += v2[v4 - 1][v3 + 1]
        for v4 in range(1, len(a1)):
            for v3 in range(1, len(a1[0])):
                v5[v4][v3] += v5[v4 - 1][v3 - 1]
        v6 = []
        v7 = set()
        for v8 in range((min(len(a1), len(a1[0])) + 1) // 2):
            for v4 in range(v8, len(a1) - v8):
                for v3 in range(v8, len(a1[0]) - v8):
                    v9 = v2[v4][v3 - v8] - v2[v4 - v8][v3] + (v5[v4][v3 + v8] - v5[v4 - v8][v3]) + a1[v4 - v8][v3] + (v2[v4 + v8][v3] - v2[v4][v3 + v8] + (v5[v4 + v8][v3] - v5[v4][v3 - v8]) - a1[v4 + v8][v3]) if v8 else a1[v4][v3]
                    if v9 in v7:
                        continue
                    v7.add(v9)
                    heapq.heappush(v6, v9)
                    if len(v6) == v1 + 1:
                        v7.remove(heapq.heappop(v6))
        v6.sort(reverse=True)
        return v6
