import heapq

class C1(object):

    def minimumPairRemoval(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return 0
        v2 = [-1] * v1
        for v3 in range(1, v1):
            v2[v3] = v3 - 1
        v4 = [v3 + 1 for v3 in range(v1 - 1)] + [-1]
        v5 = [True] * v1
        v6 = sum((a1[v3] > a1[v3 + 1] for v3 in range(v1 - 1)))
        v7 = [0] * v1
        v8 = []
        for v3 in range(v1 - 1):
            heapq.heappush(v8, (a1[v3] + a1[v3 + 1], v7[v3], v3))
        v9 = 0
        while v6 > 0:
            while v8:
                v10, v11, v12 = heapq.heappop(v8)
                v13 = v4[v12]
                if v13 == -1 or not v5[v12] or (not v5[v13]) or (v2[v13] != v12) or (v11 != v7[v12]):
                    continue
                v14 = v2[v12]
                v15 = v14 != -1 and v5[v14]
                v16 = v4[v13]
                v17 = v16 != -1 and v5[v16]
                if v15 and a1[v14] > a1[v12]:
                    v6 -= 1
                if a1[v12] > a1[v13]:
                    v6 -= 1
                if v17 and a1[v13] > a1[v16]:
                    v6 -= 1
                a1[v12] += a1[v13]
                v4[v12] = v16
                if v17:
                    v2[v16] = v12
                v5[v13] = False
                if v15 and a1[v14] > a1[v12]:
                    v6 += 1
                if v17 and a1[v12] > a1[v16]:
                    v6 += 1
                if v15:
                    v7[v14] += 1
                    heapq.heappush(v8, (a1[v14] + a1[v12], v7[v14], v14))
                if v17:
                    v7[v12] += 1
                    heapq.heappush(v8, (a1[v12] + a1[v16], v7[v12], v12))
                v9 += 1
                break
            else:
                break
        return v9
