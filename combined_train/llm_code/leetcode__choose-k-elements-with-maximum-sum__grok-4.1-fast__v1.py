import heapq

class C1:

    def findMaxSum(self, a1, a2, a3):
        v1 = len(a1)
        v2 = [0] * v1
        v3 = sorted(range(v1), key=lambda idx: a1[idx])
        v4 = []
        v5 = 0
        v6 = 0
        while v6 < v1:
            v7 = a1[v3[v6]]
            v8 = v6
            while v6 < v1 and a1[v3[v6]] == v7:
                v6 += 1
            for v9 in range(v8, v6):
                v2[v3[v9]] = v5
            for v9 in range(v8, v6):
                v10 = a2[v3[v9]]
                v5 += v10
                heapq.heappush(v4, v10)
                if len(v4) == a3 + 1:
                    v5 -= heapq.heappop(v4)
        return v2
