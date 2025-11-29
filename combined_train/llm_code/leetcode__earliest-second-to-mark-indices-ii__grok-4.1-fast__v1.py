import heapq

class C1:

    def earliestSecondToMarkIndices(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        v3 = [-1] * v1
        for v4 in range(v2 - 1, -1, -1):
            v5 = a2[v4] - 1
            if a1[v5] and v3[v5] == -1:
                v3[v5] = v4
        v6 = sum(a1) + v1
        v7 = sum((a1[i] if v3[i] == -1 else 1 for v8 in range(v1))) + v1

        def feasible(a1):
            v1 = []
            v2 = 0
            for v3 in range(a1 - 1, -1, -1):
                v4 = a2[v3] - 1
                if v3[v4] != v3:
                    v2 += 1
                    continue
                heapq.heappush(v1, a1[v4])
                if v2:
                    v2 -= 1
                else:
                    v2 += 1
                    if v1:
                        heapq.heappop(v1)
            v5 = sum(v1) + len(v1)
            return v6 - v5 <= v2
        v9, v10 = (v7, v2)
        while v9 < v10:
            v11 = v9 + (v10 - v9) // 2
            if feasible(v11):
                v10 = v11
            else:
                v9 = v11 + 1
        return v9 if v9 <= v2 and feasible(v9) else -1
