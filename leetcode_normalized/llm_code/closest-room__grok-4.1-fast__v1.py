from sortedcontainers import SortedList

class C1:

    def closestRoom(self, a1, a2):
        a1.sort(key=lambda x: -x[1])
        v1 = [(q[1], q[0], i) for v2, v3 in enumerate(a2)]
        v1.sort(reverse=True)
        v4 = SortedList()
        v5 = [-1] * len(a2)
        v6 = 0
        for v7, v8, v9 in v1:
            while v6 < len(a1) and a1[v6][1] >= v7:
                v4.add(a1[v6][0])
                v6 += 1
            if not v4:
                continue
            v10 = v4.bisect_right(v8)
            v11 = -1
            v12 = float('inf')
            if v10 < len(v4):
                v13 = abs(v4[v10] - v8)
                if v13 < v12:
                    v12 = v13
                    v11 = v4[v10]
            if v10 > 0:
                v13 = abs(v4[v10 - 1] - v8)
                if v13 < v12:
                    v12 = v13
                    v11 = v4[v10 - 1]
                elif v13 == v12:
                    v11 = min(v11, v4[v10 - 1])
            v5[v9] = v11
        return v5
