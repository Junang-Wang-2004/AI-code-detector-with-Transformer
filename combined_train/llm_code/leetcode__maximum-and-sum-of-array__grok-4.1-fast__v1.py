class C1(object):

    def maximumANDSum(self, a1, a2):
        v1 = 2 * a2
        a1 += [0] * (v1 - len(a1))
        v3 = 2 * v1 + 2
        v4 = 2 * v1
        v5 = 2 * v1 + 1
        v6 = 10 ** 18
        v7 = [[] for v8 in range(v3)]

        def add_edge(a1, a2, a3, a4):
            v7[a1].append([a2, a3, a4, len(v7[a2])])
            v7[a2].append([a1, 0, -a4, len(v7[a1]) - 1])
        for v9 in range(v1):
            add_edge(v4, v9, 1, 0)
        for v10 in range(v1):
            add_edge(v1 + v10, v5, 1, 0)
        for v9 in range(v1):
            for v10 in range(v1):
                v11 = 1 + v10 // 2
                v12 = -(a1[v9] & v11)
                add_edge(v9, v1 + v10, 1, v12)
        v13 = [0] * v3
        v14 = [0] * v3
        v15 = [0] * v3
        v16 = [0] * v3
        import heapq
        v17 = 0
        v18 = v1
        while v18 > 0:
            v14[:] = [v6] * v3
            v14[v4] = 0
            v19 = [(0, v4)]
            while v19:
                v20 = heapq.heappop(v19)
                v21, v22 = (v20[0], v20[1])
                if v21 > v14[v22]:
                    continue
                for v9 in range(len(v7[v22])):
                    v23 = v7[v22][v9]
                    if v23[1] > 0:
                        v24 = v23[0]
                        v25 = v23[2] + v13[v22] - v13[v24]
                        if v14[v24] > v14[v22] + v25:
                            v26 = v14[v22] + v25
                            v14[v24] = v26
                            v15[v24] = v22
                            v16[v24] = v9
                            heapq.heappush(v19, (v26, v24))
            if v14[v5] == v6:
                break
            for v22 in range(v3):
                if v14[v22] < v6:
                    v13[v22] += v14[v22]
            v27 = v18
            v22 = v5
            while v22 != v4:
                v27 = min(v27, v7[v15[v22]][v16[v22]][1])
                v22 = v15[v22]
            v18 -= v27
            v17 += v27 * v13[v5]
            v22 = v5
            while v22 != v4:
                v28 = v7[v15[v22]][v16[v22]]
                v28[1] -= v27
                v29 = v7[v22][v28[3]]
                v29[1] += v27
                v22 = v15[v22]
        return -v17
