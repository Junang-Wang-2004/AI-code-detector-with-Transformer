class C1:

    def subArrayRanges(self, a1):
        v1 = len(a1)
        v2 = 0
        v3 = [-1] * v1
        v4 = []
        for v5 in range(v1):
            while v4 and a1[v4[-1]] <= a1[v5]:
                v4.pop()
            if v4:
                v3[v5] = v4[-1]
            v4.append(v5)
        v6 = [v1] * v1
        v4 = []
        for v5 in range(v1 - 1, -1, -1):
            while v4 and a1[v4[-1]] < a1[v5]:
                v4.pop()
            if v4:
                v6[v5] = v4[-1]
            v4.append(v5)
        for v5 in range(v1):
            v7 = v5 - v3[v5]
            v8 = v6[v5] - v5
            v2 += a1[v5] * v7 * v8
        v3 = [-1] * v1
        v4 = []
        for v5 in range(v1):
            while v4 and a1[v4[-1]] >= a1[v5]:
                v4.pop()
            if v4:
                v3[v5] = v4[-1]
            v4.append(v5)
        v6 = [v1] * v1
        v4 = []
        for v5 in range(v1 - 1, -1, -1):
            while v4 and a1[v4[-1]] > a1[v5]:
                v4.pop()
            if v4:
                v6[v5] = v4[-1]
            v4.append(v5)
        for v5 in range(v1):
            v7 = v5 - v3[v5]
            v8 = v6[v5] - v5
            v2 -= a1[v5] * v7 * v8
        return v2
