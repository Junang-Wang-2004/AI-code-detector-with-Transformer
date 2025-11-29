class C1(object):

    def maximumRemovals(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4):
            v1 = 0
            for v2 in range(len(a1)):
                if a3[v2] <= a4 or a1[v2] != a2[v1]:
                    continue
                v1 += 1
                if v1 == len(a2):
                    return True
            return False
        v1 = [float('inf')] * len(a1)
        for v2, v3 in enumerate(a3):
            v1[v3] = v2 + 1
        v4, v5 = (0, len(a3))
        while v4 <= v5:
            v6 = v4 + (v5 - v4) // 2
            if not check(a1, a2, v1, v6):
                v5 = v6 - 1
            else:
                v4 = v6 + 1
        return v5
