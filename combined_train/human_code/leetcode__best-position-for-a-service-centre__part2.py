class C1(object):

    def getMinDistSum(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = 1e-06

        def dist(a1, a2):
            return sum((((a2[0] - x) ** 2 + (a2[1] - y) ** 2) ** 0.5 for v1, v2 in a1))
        v3 = [0.0, 0.0]
        v3[0] = float(sum((x for v4, v5 in a1))) / len(a1)
        v3[1] = float(sum((y for v5, v6 in a1))) / len(a1)
        v7 = dist(a1, v3)
        v8 = float(max(max(a1, key=lambda x: v4[0])[0], max(a1, key=lambda x: v4[1])[1])) - float(min(min(a1, key=lambda x: v4[0])[0], min(a1, key=lambda x: v4[1])[1]))
        while v8 > v2:
            for v9, v10 in v1:
                v11 = [v3[0] + v8 * v9, v3[1] + v8 * v10]
                v12 = dist(a1, v11)
                if v12 < v7:
                    v7 = v12
                    v3 = v11
                    break
            else:
                v8 /= 2.0
        return v7
