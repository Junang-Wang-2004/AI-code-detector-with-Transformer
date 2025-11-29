import heapq

class C1:

    def findShortestWay(self, a1, a2, a3):
        v1, v2 = a2
        v3, v4 = a3
        v5, v6 = (len(a1), len(a1[0]))
        v7 = [('d', 1, 0), ('l', 0, -1), ('r', 0, 1), ('u', -1, 0)]

        def slide(a1, a2, a3, a4):
            v1, v2, v3 = (a1, a2, 0)
            while 0 <= v1 + a3 < v5 and 0 <= v2 + a4 < v6 and (not a1[v1 + a3][v2 + a4]):
                v1 += a3
                v2 += a4
                v3 += 1
                if v1 == v3 and v2 == v4:
                    return (v1, v2, v3)
            return (v1, v2, v3)
        v8 = []
        heapq.heappush(v8, (0, '', v1, v2))
        v9 = set()
        while v8:
            v10, v11, v12, v13 = heapq.heappop(v8)
            v14 = (v12, v13)
            if v14 in v9:
                continue
            v9.add(v14)
            if v12 == v3 and v13 == v4:
                return v11
            for v15, v16, v17 in v7:
                v18, v19, v20 = slide(v12, v13, v16, v17)
                heapq.heappush(v8, (v10 + v20, v11 + v15, v18, v19))
        return 'impossible'
