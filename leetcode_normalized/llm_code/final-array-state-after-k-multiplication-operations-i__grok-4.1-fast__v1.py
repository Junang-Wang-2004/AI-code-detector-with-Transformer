import heapq

class C1(object):

    def getFinalState(self, a1, a2, a3):
        if a3 == 1:
            return a1
        v1 = len(a1)
        v2 = [(a1[i], i) for v3 in range(v1)]
        heapq.heapify(v2)
        v4 = max(a1)
        v5 = 0
        while v5 < a2:
            v6, v7 = v2[0]
            if v6 * a3 > v4:
                break
            heapq.heappop(v2)
            heapq.heappush(v2, (v6 * a3, v7))
            v5 += 1
        v8 = a2 - v5
        v9 = []
        while v2:
            v9.append(heapq.heappop(v2))
        v10, v11 = divmod(v8, v1)
        v12 = pow(a3, v10)
        v13 = [0] * v1
        for v14 in range(v1):
            v15, v7 = v9[v14]
            v16 = a3 if v14 < v11 else 1
            v13[v7] = v15 * v12 * v16
        return v13
