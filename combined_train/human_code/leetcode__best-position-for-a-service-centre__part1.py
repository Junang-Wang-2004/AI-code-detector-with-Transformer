class C1(object):

    def getMinDistSum(self, a1):
        """
        """
        v1 = 1e-06

        def norm(a1, a2):
            return ((a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2) ** 0.5

        def geometry_median(a1, a2):
            v1, v2 = ([0.0, 0.0], 0.0)
            for v3 in a1:
                v4 = norm(a2, v3)
                if not v4:
                    continue
                v1[0] += v3[0] / v4
                v1[1] += v3[1] / v4
                v2 += 1 / v4
            if v2 == 0.0:
                return (True, None)
            return (False, [v1[0] / v2, v1[1] / v2])
        v2 = [float(sum((p[0] for v3 in a1))) / len(a1), float(sum((v3[1] for v3 in a1))) / len(a1)]
        v4 = [float('-inf'), float('-inf')]
        while norm(v2, v4) * len(a1) > v1:
            v5, v6 = geometry_median(a1, v2)
            if v5:
                break
            v2, v4 = (v6, v2)
        return sum((norm(v2, v3) for v3 in a1))
