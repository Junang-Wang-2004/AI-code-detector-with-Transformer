import heapq
from collections import Counter

class C1:

    def minimumCost(self, a1, a2, a3):
        if a2 == 1:
            return a1[0]
        v1 = 0
        v2 = float('inf')
        v3 = []
        v4 = []
        v5 = Counter()
        v6 = Counter()
        v7 = [0]
        v8 = [0]
        for v9 in range(1, len(a1)):
            v10 = a1[v9]
            heapq.heappush(v3, -v10)
            v1 += v10
            while len(v3) - v7[0] > a2 - 1:
                while v3 and v3[0] in v5:
                    v11 = heapq.heappop(v3)
                    v5[v11] -= 1
                    if v5[v11] == 0:
                        del v5[v11]
                    v7[0] -= 1
                if v3:
                    v11 = heapq.heappop(v3)
                    v12 = -v11
                    heapq.heappush(v4, v12)
                    v1 -= v12
            if v9 > a3 + 1:
                v13 = a1[v9 - a3 - 1]
                while v4 and v4[0] in v6:
                    v11 = heapq.heappop(v4)
                    v6[v11] -= 1
                    if v6[v11] == 0:
                        del v6[v11]
                    v8[0] -= 1
                if v4 and v4[0] <= v13:
                    v6[v13] += 1
                    v8[0] += 1
                else:
                    v5[-v13] += 1
                    v7[0] += 1
                    v11 = heapq.heappop(v4)
                    v1 -= v13 - v11
                    heapq.heappush(v3, -v11)
                if v7[0] > len(v3) // 2:
                    v14 = []
                    for v15 in v3:
                        if v15 in v5:
                            v5[v15] -= 1
                            if v5[v15] == 0:
                                del v5[v15]
                        else:
                            v14.append(v15)
                    v3[:] = v14
                    heapq.heapify(v3)
                    v7[0] = 0
                if v8[0] > len(v4) // 2:
                    v16 = []
                    for v15 in v4:
                        if v15 in v6:
                            v6[v15] -= 1
                            if v6[v15] == 0:
                                del v6[v15]
                        else:
                            v16.append(v15)
                    v4[:] = v16
                    heapq.heapify(v4)
                    v8[0] = 0
            while v3 and v3[0] in v5:
                v11 = heapq.heappop(v3)
                v5[v11] -= 1
                if v5[v11] == 0:
                    del v5[v11]
                v7[0] -= 1
            if len(v3) - v7[0] == a2 - 1:
                v2 = min(v2, v1)
        return a1[0] + v2
