class C1(object):

    def scoreOfStudents(self, a1, a2):
        """
        """
        v1 = 1000
        v2 = (len(a1) + 1) // 2
        v3 = [[set() for v4 in range(v2)] for v4 in range(v2)]
        for v5 in range(v2):
            v3[v5][v5].add(int(a1[v5 * 2]))
        for v6 in range(1, v2):
            for v7 in range(v2 - v6):
                v8 = v7 + v6
                for v9 in range(v7, v8):
                    if a1[2 * v9 + 1] == '+':
                        v3[v7][v8].update((x + y for v10 in v3[v7][v9] for v11 in v3[v9 + 1][v8] if v10 + v11 <= v1))
                    else:
                        v3[v7][v8].update((v10 * v11 for v10 in v3[v7][v9] for v11 in v3[v9 + 1][v8] if v10 * v11 <= v1))
        v12 = eval(a1)
        return sum((5 if ans == v12 else 2 if ans in v3[0][-1] else 0 for v13 in a2))
