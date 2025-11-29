class C1(object):

    def mostExpensiveItem(self, a1, a2):
        """
        """
        v1 = [False] * max(a1, a2)
        v1[0] = True
        v2 = 1
        for v3 in range(2, a1 * a2):
            v1[v3 % len(v1)] = v1[(v3 - a1) % len(v1)] or v1[(v3 - a2) % len(v1)]
            if not v1[v3 % len(v1)]:
                v2 = v3
        return v2
