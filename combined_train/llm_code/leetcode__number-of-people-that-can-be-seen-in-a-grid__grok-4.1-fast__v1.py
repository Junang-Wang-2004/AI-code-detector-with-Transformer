class C1:

    def seePeople(self, a1):
        if not a1 or not a1[0]:
            return []
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [[0] * v2 for v4 in range(v1)]

        def right_vis(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3 = []
            for v4 in range(v1 - 1, -1, -1):
                v5 = a1[v4]
                v6 = 0
                while v3 and v3[-1] < v5:
                    v3.pop()
                    v6 += 1
                if v3:
                    v6 += 1
                if not v3 or v3[-1] != v5:
                    v3.append(v5)
                v2[v4] = v6
            return v2
        for v5 in range(v1):
            v6 = right_vis(a1[v5])
            for v7 in range(v2):
                v3[v5][v7] += v6[v7]
        for v7 in range(v2):
            v8 = [a1[v5][v7] for v5 in range(v1)]
            v9 = right_vis(v8)
            for v5 in range(v1):
                v3[v5][v7] += v9[v5]
        return v3
