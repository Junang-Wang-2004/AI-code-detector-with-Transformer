class C1:

    def maximizeSquareHoleArea(self, a1, a2, a3, a4):

        def largest_possible_side(a1):
            if not a1:
                return 1
            v1 = sorted(set(a1))
            if len(v1) == 0:
                return 1
            v2 = 1
            v3 = 1
            for v4 in range(1, len(v1)):
                if v1[v4] == v1[v4 - 1] + 1:
                    v3 += 1
                else:
                    v3 = 1
                v2 = max(v2, v3)
            return v2 + 1
        v1 = largest_possible_side(a3)
        v2 = largest_possible_side(a4)
        v3 = min(v1, v2)
        return v3 * v3
