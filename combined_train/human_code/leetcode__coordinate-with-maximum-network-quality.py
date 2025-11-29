class C1(object):

    def bestCoordinate(self, a1, a2):
        """
        """
        v1 = min(a1, key=lambda x: x[0])[0]
        v2 = max(a1, key=lambda x: x[0])[0]
        v3 = min(a1, key=lambda x: x[1])[1]
        v4 = max(a1, key=lambda x: x[1])[1]
        v5 = 0
        for v6 in range(v1, v2 + 1):
            for v7 in range(v3, v4 + 1):
                v8 = 0
                for v9, v10, v11 in a1:
                    v12 = ((v9 - v6) ** 2 + (v10 - v7) ** 2) ** 0.5
                    if v12 <= a2:
                        v8 += int(v11 / (1 + v12))
                if v8 > v5:
                    v5 = v8
                    v13 = (v6, v7)
        return v13
