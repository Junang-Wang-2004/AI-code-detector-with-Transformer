class C1(object):

    def maximalRectangle(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        v4 = [0] * v2
        for v5 in range(v1):
            for v6 in range(v2):
                if a1[v5][v6] == '1':
                    v4[v6] += 1
                else:
                    v4[v6] = 0
            v7 = []
            for v8 in range(v2 + 1):
                while v7 and (v8 == v2 or v4[v7[-1]] >= v4[v8]):
                    v9 = v4[v7.pop()]
                    v10 = v7[-1] if v7 else -1
                    v11 = v8 - v10 - 1
                    v3 = max(v3, v9 * v11)
                if v8 < v2:
                    v7.append(v8)
        return v3
