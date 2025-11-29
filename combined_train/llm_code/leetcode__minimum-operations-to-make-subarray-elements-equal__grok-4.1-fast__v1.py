from sortedcontainers import SortedList

class C1:

    def minOperations(self, a1, a2):
        v1 = SortedList()
        v2 = SortedList()
        v3 = v4 = 0
        v5 = float('inf')
        for v6, v7 in enumerate(a1):
            if v1 and -v1[0][0] > v7:
                v1.add((-v7, -v6))
                v3 += v7
            else:
                v2.add((v7, v6))
                v4 += v7
            while len(v1) > len(v2):
                v8, v9 = v1.pop(0)
                v3 += v8
                v2.add((-v8, -v9))
                v4 -= v8
            while len(v2) > len(v1) + 1:
                v8, v9 = v2.pop(0)
                v4 -= v8
                v1.add((-v8, -v9))
                v3 += v8
            if v6 >= a2 - 1:
                v10 = v4 - v3
                if a2 % 2:
                    v10 -= v2[0][0]
                v5 = min(v5, v10)
                v11 = v6 - a2 + 1
                v12 = a1[v11]
                v13 = (-v12, -v11)
                if v13 in v1:
                    v1.remove(v13)
                    v3 -= v12
                else:
                    v14 = (v12, v11)
                    v2.remove(v14)
                    v4 -= v12
                while len(v1) > len(v2):
                    v8, v9 = v1.pop(0)
                    v3 += v8
                    v2.add((-v8, -v9))
                    v4 -= v8
                while len(v2) > len(v1) + 1:
                    v8, v9 = v2.pop(0)
                    v4 -= v8
                    v1.add((-v8, -v9))
                    v3 += v8
        return v5
