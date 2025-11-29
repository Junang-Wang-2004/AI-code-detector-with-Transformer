class C1(object):

    def minimumObstacles(self, a1):
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
                for v7, v8 in v1:
                    v9 = (a2[0] + v7, a2[1] + v8)
                    if not (0 <= v9[0] < len(a1) and 0 <= v9[1] < len(a1[0]) and (v9 not in v5)):
                        continue
                    (v3 if not a1[v9[0]][v9[1]] else v4).append(v9)
            return -1
        return a_star(a1, (0, 0), (len(a1) - 1, len(a1[0]) - 1))
