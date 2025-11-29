import heapq

class C1:

    def amountPainted(self, a1):
        v1 = len(a1)
        v2 = []
        for v3 in range(v1):
            v4, v5 = a1[v3]
            v2.append((v4, 0, v3, v5))
            v2.append((v5, 1, v3, v5))
        v2.sort()
        v6 = [0] * v1
        v7 = []
        v8 = None
        v9 = 0
        v10 = len(v2)
        while v9 < v10:
            v11 = v2[v9][0]
            if v8 is not None:
                while v7 and v7[0][1] < v11:
                    heapq.heappop(v7)
                if v7:
                    v6[v7[0][0]] += v11 - v8
            v8 = v11
            while v9 < v10 and v2[v9][0] == v11:
                v12 = v2[v9][1]
                v13 = v2[v9][2]
                if v12 == 0:
                    heapq.heappush(v7, (v13, v2[v9][3]))
                v9 += 1
        return v6
