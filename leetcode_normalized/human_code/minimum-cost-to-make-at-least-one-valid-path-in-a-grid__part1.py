class C1(object):

    def minCost(self, a1):
        """
        """
        v1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def a_star(a1, a2, a3):
            v1, v2 = (0, 1)
            v3, v4 = ([a2], [])
            v5 = set()
            while v3 or v4:
                if not v3:
                    v1 += v2
                    v3, v4 = (v4, v3)
                a2 = v3.pop()
                if a2 in v5:
                    continue
                v5.add(a2)
                if a2 == a3:
                    return v1
                for v7, (v8, v9) in enumerate(v1, 1):
                    v10 = (a2[0] + v8, a2[1] + v9)
                    if not (0 <= v10[0] < len(a1) and 0 <= v10[1] < len(a1[0]) and (v10 not in v5)):
                        continue
                    (v3 if v7 == a1[a2[0]][a2[1]] else v4).append(v10)
            return -1
        return a_star(a1, (0, 0), (len(a1) - 1, len(a1[0]) - 1))
