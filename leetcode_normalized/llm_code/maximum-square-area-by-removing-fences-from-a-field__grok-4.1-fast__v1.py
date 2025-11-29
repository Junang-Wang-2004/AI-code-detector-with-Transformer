class C1(object):

    def maximizeSquareArea(self, a1, a2, a3, a4):
        v1 = 10 ** 9 + 7

        def possible_sides(a1, a2):
            v1 = sorted(set(a1 + [1, a2]))
            v2 = set()
            for v3 in range(len(v1)):
                for v4 in range(v3 + 1, len(v1)):
                    v2.add(v1[v4] - v1[v3])
            return v2
        v2 = possible_sides(a3, a1)
        v3 = possible_sides(a4, a2)
        v4 = max((s for v5 in v2 if v5 in v3), default=-1)
        return v4 * v4 % v1 if v4 != -1 else -1
