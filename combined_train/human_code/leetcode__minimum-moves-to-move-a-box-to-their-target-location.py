class C1(object):

    def minPushBox(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dot(a1, a2):
            return a1[0] * a2[0] + a1[1] * a2[1]

        def can_reach(a1, a2, a3, a4):
            v1, v2 = ([a3], [])
            v3 = set([a2])
            while v1 or v2:
                if not v1:
                    v1, v2 = (v2, v1)
                a3 = v1.pop()
                if a3 == a4:
                    return True
                if a3 in v3:
                    continue
                v3.add(a3)
                for v5, v6 in v1:
                    v7 = (a3[0] + v5, a3[1] + v6)
                    if not (0 <= v7[0] < len(a1) and 0 <= v7[1] < len(a1[0]) and (a1[v7[0]][v7[1]] != '#') and (v7 not in v3)):
                        continue
                    (v1 if dot((v5, v6), (a4[0] - a3[0], a4[1] - a3[1])) > 0 else v2).append(v7)
            return False

        def g(a1, a2):
            return abs(a1[0] - a2[0]) + abs(a1[1] - a2[1])

        def a_star(a1, a2, a3, a4):
            v1, v2 = (g(a2, a4), 2)
            v3, v4 = ([(a2, a3)], [])
            v5 = set()
            while v3 or v4:
                if not v3:
                    v1 += v2
                    v3, v4 = (v4, v3)
                a2, a3 = v3.pop()
                if a2 == a4:
                    return v1
                if (a2, a3) in v5:
                    continue
                v5.add((a2, a3))
                for v8, v9 in v1:
                    v10, v11 = ((a2[0] + v8, a2[1] + v9), (a2[0] - v8, a2[1] - v9))
                    if not (0 <= v10[0] < len(a1) and 0 <= v10[1] < len(a1[0]) and (0 <= v11[0] < len(a1)) and (0 <= v11[1] < len(a1[0])) and (a1[v10[0]][v10[1]] != '#') and (a1[v11[0]][v11[1]] != '#') and ((v10, a2) not in v5) and can_reach(a1, a2, a3, v11)):
                        continue
                    (v3 if dot((v8, v9), (a4[0] - a2[0], a4[1] - a2[1])) > 0 else v4).append((v10, a2))
            return -1
        v2, v3, v4 = (None, None, None)
        for v5 in range(len(a1)):
            for v6 in range(len(a1[0])):
                if a1[v5][v6] == 'B':
                    v2 = (v5, v6)
                elif a1[v5][v6] == 'S':
                    v3 = (v5, v6)
                elif a1[v5][v6] == 'T':
                    v4 = (v5, v6)
        return a_star(a1, v2, v3, v4)
