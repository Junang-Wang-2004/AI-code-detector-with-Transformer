class C1(object):

    def maximumMinimumPath(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def check(a1, a2, a3, a4, a5):
            if a3 == len(a1) - 1 and a4 == len(a1[0]) - 1:
                return True
            a5.add((a3, a4))
            for v1 in v1:
                v2, v3 = (a3 + v1[0], a4 + v1[1])
                if 0 <= v2 < len(a1) and 0 <= v3 < len(a1[0]) and ((v2, v3) not in a5) and (a1[v2][v3] >= a2) and check(a1, a2, v2, v3, a5):
                    return True
            return False
        v2, v3 = ([], min(a1[0][0], a1[-1][-1]))
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                if a1[v4][v5] <= v3:
                    v2.append(a1[v4][v5])
        v2 = list(set(v2))
        v2.sort()
        v6, v7 = (0, len(v2) - 1)
        while v6 <= v7:
            v8 = v6 + (v7 - v6) // 2
            if not check(a1, v2[v8], 0, 0, set()):
                v7 = v8 - 1
            else:
                v6 = v8 + 1
        return v2[v7]
