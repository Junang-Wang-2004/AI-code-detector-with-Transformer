class C1(object):

    def sumOfBeauties(self, a1):
        """
        """
        v1 = [a1[-1]] * len(a1)
        for v2 in reversed(range(2, len(a1) - 1)):
            v1[v2] = min(v1[v2 + 1], a1[v2])
        v3, v4 = (0, a1[0])
        for v2 in range(1, len(a1) - 1):
            if v4 < a1[v2] < v1[v2 + 1]:
                v3 += 2
            elif a1[v2 - 1] < a1[v2] < a1[v2 + 1]:
                v3 += 1
            v4 = max(v4, a1[v2])
        return v3
