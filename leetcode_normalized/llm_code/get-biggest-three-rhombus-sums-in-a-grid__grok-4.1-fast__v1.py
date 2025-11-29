class C1:

    def getBiggestThree(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]
        v5 = [[0] * v2 for v4 in range(v1)]
        for v6 in range(v1):
            for v7 in range(v2):
                v3[v6][v7] = a1[v6][v7]
        for v6 in range(1, v1):
            for v7 in range(v2 - 1):
                v3[v6][v7] += v3[v6 - 1][v7 + 1]
        for v6 in range(v1):
            for v7 in range(v2):
                v5[v6][v7] = a1[v6][v7]
        for v6 in range(1, v1):
            for v7 in range(1, v2):
                v5[v6][v7] += v5[v6 - 1][v7 - 1]
        import heapq
        v8 = []
        v9 = set()
        v10 = 3
        v11 = (min(v1, v2) + 1) // 2
        for v12 in range(v11):
            for v13 in range(v12, v1 - v12):
                for v14 in range(v12, v2 - v12):
                    if v12 == 0:
                        v15 = a1[v13][v14]
                    else:
                        v16 = v3[v13][v14 - v12] - v3[v13 - v12][v14]
                        v17 = v5[v13][v14 + v12] - v5[v13 - v12][v14]
                        v18 = a1[v13 - v12][v14]
                        v19 = v16 + v17 + v18
                        v20 = v3[v13 + v12][v14] - v3[v13][v14 + v12]
                        v21 = v5[v13 + v12][v14] - v5[v13][v14 - v12]
                        v22 = a1[v13 + v12][v14]
                        v23 = v20 + v21 - v22
                        v15 = v19 + v23
                    if v15 in v9:
                        continue
                    v9.add(v15)
                    heapq.heappush(v8, v15)
                    if len(v8) > v10:
                        heapq.heappop(v8)
                        v9.remove(v8[0])
        v8.sort(reverse=True)
        return v8
