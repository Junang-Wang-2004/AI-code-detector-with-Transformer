import heapq

class C1:

    def minTime(self, a1, a2, a3, a4, a5):
        v1 = (1 << a1) - 1
        v2 = float('inf')
        v3 = [0] * (1 << a1)
        for v4 in range(a1):
            v5 = 1 << v4
            for v6 in range(1 << a1):
                if v6 & v5:
                    v3[v6] = max(v3[v6], a4[v4])
        v7 = [bin(v4).count('1') for v4 in range(1 << a1)]
        v8 = [[[v2] * (1 << a1) for v9 in range(a3)] for v9 in range(2)]
        v10 = []
        v8[0][0][v1] = 0.0
        heapq.heappush(v10, (0.0, 0, 0, v1))
        while v10:
            v11, v12, v13, v6 = heapq.heappop(v10)
            if v11 > v8[v12][v13][v6]:
                continue
            if v6 == 0:
                return v11
            if v12 == 0:
                v14 = v6
                while v14 > 0:
                    if v7[v14] <= a2:
                        v15 = v3[v14] * a5[v13]
                        v16 = 1
                        v17 = (v13 + int(v15)) % a3
                        v18 = v6 ^ v14
                        v19 = v11 + v15
                        if v8[v16][v17][v18] > v19:
                            v8[v16][v17][v18] = v19
                            heapq.heappush(v10, (v19, v16, v17, v18))
                    v14 = v14 - 1 & v6
            else:
                for v4 in range(a1):
                    if v6 & 1 << v4 == 0:
                        v14 = 1 << v4
                        v15 = v3[v14] * a5[v13]
                        v16 = 0
                        v17 = (v13 + int(v15)) % a3
                        v18 = v6 ^ v14
                        v19 = v11 + v15
                        if v8[v16][v17][v18] > v19:
                            v8[v16][v17][v18] = v19
                            heapq.heappush(v10, (v19, v16, v17, v18))
        return -1.0
