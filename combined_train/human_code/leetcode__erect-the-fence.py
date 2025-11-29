class C1(object):

    def outerTrees(self, a1):
        """
        """
        a1 = sorted(set((tuple(x) for v2 in a1)))
        if len(a1) <= 1:
            return a1

        def cross(a1, a2, a3):
            return (a2[0] - a1[0]) * (a3[1] - a1[1]) - (a2[1] - a1[1]) * (a3[0] - a1[0])
        v3 = []
        for v4 in a1:
            while len(v3) >= 2 and cross(v3[-2], v3[-1], v4) < 0:
                v3.pop()
            v3.append(v4)
        v5 = []
        for v4 in reversed(a1):
            while len(v5) >= 2 and cross(v5[-2], v5[-1], v4) < 0:
                v5.pop()
            v5.append(v4)
        v6 = v3[:-1] + v5[:-1]
        return v6 if v6[1] != v6[-1] else v6[:len(v6) // 2 + 1]
