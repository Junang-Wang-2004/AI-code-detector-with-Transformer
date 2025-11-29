class C1:

    def minConnectedGroups(self, a1, a2):
        a1.sort(key=lambda x: x[0])
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = []
        v3 = float('-inf')
        for v4 in range(v1):
            if v3 < a1[v4][0]:
                v2.append(v4)
            v3 = max(v3, a1[v4][1])
        v5 = len(v2)

        def bisect_right(a1, a2):
            v1 = 0
            v2 = len(a1)
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if a1[v3] <= a2:
                    v1 = v3 + 1
                else:
                    v2 = v3
            return v1
        v6 = 0
        v7 = 0
        for v8 in range(v1):
            while v7 < v1 and a1[v8][0] - a1[v7][1] > a2:
                v7 += 1
            v9 = bisect_right(v2, v8) - bisect_right(v2, v7)
            if v9 > v6:
                v6 = v9
        return v5 - v6
