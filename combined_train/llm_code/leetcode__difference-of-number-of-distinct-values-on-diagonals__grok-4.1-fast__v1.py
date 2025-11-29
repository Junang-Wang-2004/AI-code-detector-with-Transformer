class C1(object):

    def differenceOfDistinctValues(self, a1):
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [[0] * v2 for v4 in range(v1)]

        def handle_diagonal(a1, a2):
            v1 = set()
            v2 = a1
            v3 = a2
            while v2 < v1 and v3 < v2:
                v3[v2][v3] = len(v1)
                v1.add(a1[v2][v3])
                v2 += 1
                v3 += 1
            v4 = a1
            v5 = a2
            while v4 < v1 and v5 < v2:
                v4 += 1
                v5 += 1
            v4 -= 1
            v5 -= 1
            v1 = set()
            v2 = v4
            v3 = v5
            while v2 >= a1 and v3 >= a2:
                v6 = len(v1)
                v3[v2][v3] = abs(v3[v2][v3] - v6)
                v1.add(a1[v2][v3])
                v2 -= 1
                v3 -= 1
        for v5 in range(v2):
            handle_diagonal(0, v5)
        for v6 in range(1, v1):
            handle_diagonal(v6, 0)
        return v3
