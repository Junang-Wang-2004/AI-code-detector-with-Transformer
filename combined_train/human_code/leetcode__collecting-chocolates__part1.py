class C1(object):

    def minCost(self, a1, a2):
        """
        """

        def accumulate(a1):
            for v1 in range(len(a1) - 1):
                a1[v1 + 1] += a1[v1]
            return a1
        v1 = min(range(len(a1)), key=lambda x: a1[a2])
        a1 = a1[v1:] + a1[:v1]
        v3, v4 = ([-1] * len(a1), [len(a1)] * len(a1))
        v5 = []
        for v1 in range(len(a1)):
            while v5 and a1[v5[-1]] > a1[v1]:
                v4[v5.pop()] = v1
            if v5:
                v3[v1] = v5[-1]
            v5.append(v1)
        v6 = [0] * (len(a1) + 1)
        v6[0] = +1 * sum(a1)
        v6[1] = a2
        v6[-1] += -1 * a1[0]
        for v1 in range(1, len(a1)):
            v7, v8 = (v1 - v3[v1], v4[v1] - v1)
            v6[min(v7, v8)] += -1 * a1[v1]
            v6[max(v7, v8)] += -1 * a1[v1]
            v6[v7 + v8] += +1 * a1[v1]
        return min(accumulate(accumulate(v6)))
