class C1(object):

    def shortestPath(self, a1, a2):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dot(a1, a2):
            return a1[0] * a2[0] + a1[1] * a2[1]

        def g(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])

        def a_star(a1, a2, a3, a4):
            v1, v2 = (g(a2, a3), 2)
            v3, v4 = ([(a2, a4)], [])
            v5 = {}
            while v3 or v4:
                if not v3:
                    v1 += v2
                    v3, v4 = (v4, v3)
                a2, a4 = v3.pop()
                if a2 == a3:
                    return v1
                if a2 in v5 and v5[a2] >= a4:
                    continue
                v5[a2] = a4
                for v8, v9 in v1:
                    v10 = (a2[0] + v8, a2[1] + v9)
                    if not (0 <= v10[0] < len(a1) and 0 <= v10[1] < len(a1[0]) and (a1[v10[0]][v10[1]] == 0 or a4 > 0) and (v10 not in v5 or v5[v10] < a4)):
                        continue
                    (v3 if dot((v8, v9), (a3[0] - a2[0], a3[1] - a2[1])) > 0 else v4).append((v10, a4 - int(a1[v10[0]][v10[1]] == 1)))
            return -1
        return a_star(a1, (0, 0), (len(a1) - 1, len(a1[0]) - 1), a2)
